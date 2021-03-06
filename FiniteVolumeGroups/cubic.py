import FiniteVolumeGroups.utilities as util
import numpy as np
import math
import copy


class O(util.FiniteVolumeGroup):
  def __init__(self):

    element_generators = [
        util.ElementGenerator("E", 0., [ [0,0,1] ]),

        util.ElementGenerator("C3", angle=2.*math.pi/3.,
          directions = [
            [1,1,1],[-1,1,1],[1,-1,1],[1,1,-1],[-1,-1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]
          ]),

        util.ElementGenerator("C2xyz", angle=math.pi,
          directions = [ [1,0,0], [0,1,0], [0,0,1] ]),

        util.ElementGenerator("C2diag", angle=math.pi,
          directions = [ [1,1,0], [1,-1,0], [0,1,1], [0,1,-1], [1,0,1], [1,0,-1] ]),

        util.ElementGenerator("C4", angle=math.pi/2.,
          directions = [ [1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1] ])
      ]

    self.irrep_generators = {
          "A1": [lambda x,y,z: x*x + y*y + z*z],
          "A2": [lambda x,y,z: x*y*z],
          "E":  [lambda x,y,z: x*x-y*y, lambda x,y,z: 2*z*z-x*x-y*y],
          "T1": [lambda x,y,z: x, lambda x,y,z: y, lambda x,y,z: z],
          "T2": [lambda x,y,z: x*y, lambda x,y,z: x*z, lambda x,y,z: y*z],
        }

    super().__init__(element_generators, self.irrep_generators)





class Oh(O):
  def __init__(self):
    super().__init__();

    # add parity partner elements
    self.define_o_parity()
    self.add_parity_partners()

    self.rename_o_irreps()

    self.add_opposite_parity_irreps()


  def rename_o_irreps(self):
    for elem in self.elements:
      irreps = elem.irreps
      irreps["A1g"]=irreps.pop("A1")
      irreps["A2u"]=irreps.pop("A2")
      irreps["Eg"]=irreps.pop("E")
      irreps["T1u"]=irreps.pop("T1")
      irreps["T2g"]=irreps.pop("T2")

  def define_o_parity(self):
    for elem in self.elements:
      ids = elem.identifier
      ids["parity"] = 1


  def add_parity_partners(self):
    origin_elements = copy.deepcopy(self.elements)
    for elem in origin_elements:
      ids = elem.identifier
      ids["parity"] = -1

      parity_rotation = np.matmul(np.array([[-1,0,0],[0,-1,0],[0,0,-1]]),util.rotation(ids["direction"],ids["angle"]))

      self.elements.append(
          util.GroupElement(
              ids,
              'i'+elem.conjugacy_class,
              parity_rotation,
              self.make_irreps(parity_rotation, self.irrep_generators)
            )
        )

  def add_opposite_parity_irreps(self):
    for elem in self.elements:
      irreps = elem.irreps
      parity = -1 if elem.conjugacy_class[0]=='i' else 1
      irreps["A1u"]=parity*irreps["A1g"]
      irreps["A2g"]=parity*irreps["A2u"]
      irreps["Eu"]=parity*irreps["Eg"]
      irreps["T1g"]=parity*irreps["T1u"]
      irreps["T2u"]=parity*irreps["T2g"]
