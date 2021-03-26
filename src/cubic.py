import src.utilities as util
import numpy as np
import math



class O(util.FiniteVolumeGroup):
  def __init__(self):
    
    element_generators = [
        util.ElementGenerator("E", 0., [ [0,0,1] ]),
        
        util.ElementGenerator("C3", angle=2.*math.pi/3., 
          directions = [ 
            [1,1,1],[1,-1,1],[1,-1,1],[1,1,-1],[-1,-1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1] 
          ]),

        util.ElementGenerator("C2xyz", angle=math.pi, 
          directions = [ [1,0,0], [0,1,0], [0,0,1] ]),

        util.ElementGenerator("C2diag", angle=math.pi,
          directions = [ [1,1,0], [1,-1,0], [0,1,1], [0,1,-1], [1,0,1], [1,0,-1] ]),

        util.ElementGenerator("C4", angle=math.pi/2., 
          directions = [ [1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1] ])
      ]

    irrep_generators = {
          "A1": [lambda x,y,z: x*x + y*y + z*z],
          "A2": [lambda x,y,z: x*y*z],
          "E":  [lambda x,y,z: x*x-y*y, lambda x,y,z: 2*z*z-x*x-y*y],
          "T1": [lambda x,y,z: x, lambda x,y,z: y, lambda x,y,z: z],
          "T2": [lambda x,y,z: x*y, lambda x,y,z: x*z, lambda x,y,z: y*z],
        }



    super().__init__(element_generators, irrep_generators)



    

class Oh(O):
  def __init__(self):
      
