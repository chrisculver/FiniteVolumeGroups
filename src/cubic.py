import src.utilities as util
import math

class O(util.RotationGroup):
  def __init__(self):
    # The identity
    super().__init__()

    # C2-xyz Rotations
    self.generate_elements_from( util.rotation( [1,0,0], math.pi)  )
    self.generate_elements_from( util.rotation( [0,1,0], math.pi)  )
    self.generate_elements_from( util.rotation( [0,0,1], math.pi)  )

    # C4 Rotations
    self.generate_elements_from( util.rotation( [1,0,0], math.pi/2.)  )
    self.generate_elements_from( util.rotation( [0,1,0], math.pi/2.)  )
    self.generate_elements_from( util.rotation( [0,0,1], math.pi/2.)  )

    # C2-diagonal Rotations
    self.generate_elements_from( util.rotation( [1,1,0], math.pi) )
    self.generate_elements_from( util.rotation( [0,1,1], math.pi) )
    
    # C3 rotations
    self.generate_elements_from( util.rotation( [1,1,1], 2.*math.pi/3.)  )

    # The conjugacy classes are closed

class Oh(O):
  def __init__(self):
    super().__init__()

    # this doubles the number of conjugacy classes, the original
    # conjugacy classes are parity(+)
    # this generates parity(-) classes
    self.generate_elements_from( [[-1,0,0],[0,-1,0],[0,0,-1]] )
