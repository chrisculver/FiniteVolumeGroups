import copy
import math
import numpy as np
from scipy.linalg import expm


class GroupElement():
  def __init__(self, identifier, conjugacy_class, irreps):
    self.identifier = identifier
    self.conjugacy_class = conjugacy_class
    self.irreps = irreps

  def __call__(self, irrep):
    return irreps[irrep]

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
  # TODO: CC doesn't know why they are negative
  so3_generators =  [ [[0.,0.,0.],[0.,0.,1.],[0.,-1.,0.]],
                      [[0.,0.,-1.],[0.,0.,0.],[1.,0.,0.]],
                      [[0.,1.,0.],[-1.,0.,0.],[0.,0.,0.]] ]
  
  norm_r = math.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])

  return int_matrix(expm( (np.asarray(phi*r[0])*so3_generators[0] 
              + np.asarray(phi*r[1])*so3_generators[1]
              + np.asarray(phi*r[2])*so3_generators[2])/norm_r ).tolist())


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
