from FiniteVolumeGroups.irrep import generate_irrep

import copy
import math
import numpy as np
from dataclasses import dataclass
from typing import List
from scipy.linalg import expm



@dataclass
class ElementGenerator:
  conjucacy_class_name: str
  angle: float
  directions: List[List[int]]  # a list of 3vectors specifying the direction of the rotation
  names: List[str]


class GroupElement():
  """ A group element

      :ivar identifier: Dictionary of meta data
      :ivar conjugacy_class: String
      :ivar irreps: Dictionary of matrices
      :ivar rotation: 3D representation matrix.

      The identifier keys are 'angle', 'direction' and 'parity'.
      The angle and direction are for a rotation in 3D space.
      'parity' returns the parity of the rotation or None
      if the group has no parity rotations included.
  """
  def __init__(self, identifier, conjugacy_class, rotation, irreps):
    self.identifier = identifier
    self.conjugacy_class = conjugacy_class
    self.irreps = irreps
    self.rotation = rotation

  def __call__(self, irrep):
    """ Gets the irrep of the group element

        :param irrep: String specifying the irrep
    """
    return self.irreps[irrep]



class FiniteVolumeGroup():
  """Base class for all finite volume groups.
     Just holds the group elements in a list.

     If you want to make your own group it's best to
     look at cubic.py and replicate what is done there.
  """
  def __init__(self, element_generators, irrep_generators):
    self.elements = [] #: List of the group elements
    for elem in element_generators:
      for i,direction in enumerate(elem.directions):
        self.elements.append(
            self.make_group_element(
              elem.names[i], elem.angle, direction,
              elem.conjucacy_class_name,
              irrep_generators)
        )

  # makes the group element
  def make_group_element(self, name, angle, direction, conj_class, irrep_generators):
    return GroupElement(
        {"name": name, "angle": angle, "direction": direction, "parity": None, "spinor": None},
        conj_class,
        rotation(direction, angle),
        self.make_irreps(rotation(direction, angle), irrep_generators)
      )

  # fills in the irreps of that group element
  def make_irreps(self,elem, irrep_gen):
    return {name: generate_irrep(elem, funcs) for name,funcs in irrep_gen.items()}

  def irrep(self, name):
    """ Returns the whole irrep for the group.

        :param name: String for the name of the irrep
    """
    return [ elem.irreps[name] for elem in self.elements]

  def get_element(self, name, parity=1, spinor=False):
    """ Returns the element with the matching string """
    for elem in self.elements:
      if elem.identifier['name']==name and parity==elem.identifier['parity'] and spinor==elem.identifier['spinor']:
        return elem
    return None

#DEPRECATED
#given a list of elements, apply rotations until the set is
#closed
def generate_closed_elements(elems):
  res = copy.deepcopy(elems)

  for elem in elems:
    adding_elements = True
    while(adding_elements):
      original_elements = copy.deepcopy(res)

      for r in res:
        if( matmul(elem, r) not in res ):
          res.append( matmul(elem, r) )

      if( res == original_elements ):
        adding_elements=False

  return res


#direction r and angle phi
def rotation(r, phi):
  so3_generators =  [ [[0.,0.,0.],[0.,0.,1.],[0.,-1.,0.]],
                      [[0.,0.,-1.],[0.,0.,0.],[1.,0.,0.]],
                      [[0.,1.,0.],[-1.,0.,0.],[0.,0.,0.]] ]

  norm_r = math.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])

  tmp = expm( (np.asarray(phi*r[0])*so3_generators[0]
              + np.asarray(phi*r[1])*so3_generators[1]
              + np.asarray(phi*r[2])*so3_generators[2])/norm_r ).tolist()

  tmp = np.round(np.array(tmp),8)

  return tmp.tolist()


# Converts a floating point matrix to a matrix of ints
def int_matrix(m):
  res = [[0 for elem in row] for row in m]
  for i in range(len(m)):
    for j in range(len(m[0])):
      res[i][j] = int(round(m[i][j]))
  return res


# I don't feel like making a matrix class to do x*y
def matmul(x,y):
  z = [[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]

  for i in range(len(x)):
    for j in range(len(y[0])):
      for k in range(len(y)):
        z[i][j] += x[i][k]*y[k][j]

  return z



def g1_matrix(r, phi):
    pauli_matrices = [ [[0,1],[1,0]],
                       [[0,-1j],[1j,0]],
                       [[1,0],[0,-1]] ]

    norm_r = math.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])

    tmp = expm( -1j*(np.asarray(phi*r[0])*pauli_matrices[0]
                + np.asarray(phi*r[1])*pauli_matrices[1]
                + np.asarray(phi*r[2])*pauli_matrices[2])/(2.*norm_r) ).tolist()

    tmp = np.round(np.array(tmp),8)

    return tmp


def h_matrix(r, phi):
    s32 = math.sqrt(3.)/2.
    spin32_generator = [ [[0,s32,0,0],[s32,0,1,0],[0,1,0,s32],[0,0,s32,0]],
                         [[0,-s32*1j,0,0],[s32*1j,0,-1j,0],[0,1j,0,-s32*1j],[0,0,s32*1j,0]],
                         [[3./2.,0,0,0],[0,1./2.,0,0],[0,0,-1./2.,0],[0,0,0,-3./2.]] ]

    norm_r = math.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])

    tmp = expm( -1j*(np.asarray(phi*r[0])*spin32_generator[0]
            + np.asarray(phi*r[1])*spin32_generator[1]
            + np.asarray(phi*r[2])*spin32_generator[2])/(norm_r) ).tolist()

    tmp = np.round(np.array(tmp),8)

    return tmp
