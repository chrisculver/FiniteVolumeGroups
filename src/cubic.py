import src.utilities as util
import math

## The octahedral group O.  The group elements are by default written down
## in a 3 dimensional representation
## To iterate through all the group elements do 
##    'for elem in o.elements:'
## or
##    'for class,elems in o.conjugacy_classes.items():'
##    '  for elem in elems'
class O():
  def __init__(self):

    self.elements = util.generate_closed_elements([
        # The identity
        [[1,0,0],[0,1,0],[0,0,1]],
        # C2-xyz Rotations
        util.rotation( [1,0,0], math.pi),
        util.rotation( [0,1,0], math.pi),
        util.rotation( [0,0,1], math.pi),
        # C4 Rotations
        util.rotation( [1,0,0], math.pi/2.),
        util.rotation( [0,1,0], math.pi/2.),
        util.rotation( [0,0,1], math.pi/2.),
        # C2-diagonal Rotations
        util.rotation( [1,1,0], math.pi ),
        util.rotation( [0,1,1], math.pi ),
        # C3 rotations
        util.rotation( [1,1,1], 2.*math.pi/3.)
      ])

    self.conjugacy_classes = {

        "E": [ [[1,0,0],[0,1,0],[0,0,1]] ],

        "C3": [ util.rotation( [1,1,1], 2.*math.pi/3.),
                util.rotation( [-1,1,1], 2.*math.pi/3.),
                util.rotation( [1,-1,1], 2.*math.pi/3.),
                util.rotation( [1,1,-1], 2.*math.pi/3.),
                util.rotation( [-1,-1,1], 2.*math.pi/3.),
                util.rotation( [1,-1,-1], 2.*math.pi/3.),
                util.rotation( [-1,1,-1], 2.*math.pi/3.),
                util.rotation( [-1,-1,-1], 2.*math.pi/3.),
              ],

        "C2xyz": [ util.rotation( [1,0,0], math.pi),
                   util.rotation( [0,1,0], math.pi),
                   util.rotation( [0,0,1], math.pi), 
                 ],
      
        "C2diag": [ util.rotation( [1,1,0], math.pi ),
                    util.rotation( [1,-1,0], math.pi ), 
                    util.rotation( [0,1,1], math.pi ), 
                    util.rotation( [0,1,-1], math.pi ), 
                    util.rotation( [1,0,1], math.pi ), 
                    util.rotation( [1,0,-1], math.pi ),
                  ],

        "C4": [ util.rotation( [1,0,0], math.pi/2.),
                util.rotation( [-1,0,0], math.pi/2.),
                util.rotation( [0,1,0], math.pi/2.),
                util.rotation( [0,-1,0], math.pi/2.),
                util.rotation( [0,0,1], math.pi/2.), 
                util.rotation( [0,0,-1], math.pi/2.), 
              ]  
    } # end of conjugacy class dictionary


class Oh(O):
  def __init__(self):
    super().__init__()

    # this doubles the number of conjugacy classes, the original
    # conjugacy classes are parity(+)
    # this generates parity(-) classes
    self.elements = util.generate_closed_elements(
        self.elements +  
        [ [[-1,0,0],[0,-1,0],[0,0,-1]] ] 
      )
