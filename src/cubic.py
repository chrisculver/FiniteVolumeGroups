import src.utilities as util
import math



class O():
  def __init__(self):
    self.elements = []

    add_elems = lambda angle, directions, conj : [ 
                  self.elements.append (self.make_group_element(angle, d, conj) ) 
                  for d in directions ]

    e_angle = 0.
    e_directions = [ [0,0,1] ]
    add_elems(e_angle, e_directions, "E")

    c3_angle = 2.*math.pi/3.
    c3_directions = [
        [1,1,1],[1,-1,1],[1,-1,1],[1,1,-1],[-1,-1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1] ]
    add_elems(c3_angle, c3_directions, "C3")

    c2xyz_angle = math.pi
    c2xyz_directions = [ [1,0,0], [0,1,0], [0,0,1] ]
    add_elems(c2xyz_angle, c2xyz_directions, "C2xyz")

    c2diag_angle = math.pi
    c2diag_directions = [ [1,1,0], [1,-1,0], [0,1,1], [0,1,-1], [1,0,1], [1,0,-1] ]
    add_elems(c2diag_angle, c2diag_directions, "C2diag")

    c4_angle = math.pi/2.
    c4_directions = [ [1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1] ]
    add_elems(c4_angle, c4_directions, "C4")



  def make_group_element(self, angle, direction, conj_class):
    return util.GroupElement( 
        {"angle": angle, "direction": direction},
        conj_class,
        self.make_all_irreps(angle, direction, conj_class)
      )


  def make_all_irreps(self, angle, direction, conj_class):
    return {
          "A1": 1,
          "A2": -1 if (conj_class == "C2diag") or (conj_class == "C4") else 1,
          "T1": util.rotation(direction, angle)
        }



#class Oh(O):
#  def __init__(self):
#    super().__init__()

    # this doubles the number of conjugacy classes, the original
    # conjugacy classes are parity(+)
    # this generates parity(-) classes
#    self.elements = util.generate_closed_elements(
#        self.elements +  
#        [ [[-1,0,0],[0,-1,0],[0,0,-1]] ] 
#      )
