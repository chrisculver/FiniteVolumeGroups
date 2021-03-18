import copy
import math
import numpy as np
from scipy.linalg import expm


class RotationGroup:
  def __init__(self):
    self.elements = [ [[1,0,0],[0,1,0],[0,0,1]] ]

  def generate_elements_from(self,rotation):  
    adding_elements=True

    while(adding_elements):
      original_elements = copy.deepcopy(self.elements)
     
      print("rotation = " + str(rotation))
      for elem in self.elements:
        print(elem)

      for elem in self.elements:
        if( matmul(rotation,elem) not in self.elements ):
          self.elements.append( matmul(rotation,elem) )
          # if we add an element from a rot, it may be that
          # elem.rot.rot could be an element of the group.
          # going through the loop again will check this
          
          # There's probably a shorter/better implementation using 
          # that at some point elem.rot.rot.rot.rot = elem (it's a finite group)
     
      if( self.elements == original_elements ):
        adding_elements=False

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


def int_matrix(m):
  res = [[0 for elem in row] for row in m]
  for i in range(len(m)):
    for j in range(len(m[0])):
      res[i][j] = int(m[i][j])
  return res
      

def matmul(x,y):
  z = [[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]
  
  for i in range(len(x)):
    for j in range(len(y[0])):
      for k in range(len(y)):
        z[i][j] += x[i][k]*y[k][j]

  return z
