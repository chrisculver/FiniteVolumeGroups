import FiniteVolumeGroups.utilities as util
import numpy as np
import math
import copy


class O(util.FiniteVolumeGroup):
  def __init__(self):

    # Names from Morningstar notes
    element_generators = [
            util.ElementGenerator("E", angle=0.,
                                  directions=[[0, 0, 1]],
                                  names=["E"]
                                  ),

            util.ElementGenerator("C3", angle=2.*math.pi/3.,
                                  directions=[
                                      [1, 1, 1], [-1, 1, 1], [1, -1, 1],
                                      [1, 1, -1], [-1, -1, 1], [1, -1, -1],
                                      [-1, 1, -1], [-1, -1, -1]
                                      ],
                                  names=[
                                      "C3delta", "C3gamma-1", "C3beta-1",
                                      "C3alpha-1", "C3alpha", "C3gamma",
                                      "C3beta", "C3delta-1"
                                  ]),

            util.ElementGenerator("C2xyz", angle=math.pi,
                                  directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                                  names=["C2x", "C2y", "C2z"]
                                  ),

            util.ElementGenerator("C2diag", angle=math.pi,
                                  directions=[[1, 1, 0], [
                                      1, -1, 0], [0, 1, 1], [0, 1, -1], [1, 0, 1], [-1, 0, 1]],
                                  names=["C2a", "C2b", "C2e",
                                         "C2f", "C2c", "C2d"]
                                  ),

            util.ElementGenerator("C4", angle=math.pi/2.,
                                  directions=[[1, 0, 0], [-1, 0, 0], [0, 1,
                                                                      0], [0, -1, 0], [0, 0, 1], [0, 0, -1]],
                                  names=["C4x", "C4x-1", "C4y",
                                         "C4y-1", "C4z", "C4z-1"]
                                  )
            ]

    self.irrep_generators = {
          "A1": [lambda x, y, z: x*x + y*y + z*z],
          "A2": [lambda x, y, z: x*y*z],
          "E":  [lambda x, y, z: x*x-y*y, lambda x, y, z: 2*z*z-x*x-y*y],
          "T1": [lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: z],
          "T2": [lambda x, y, z: x*y, lambda x, y, z: x*z, lambda x, y, z: y*z],
        }

    super().__init__(element_generators, self.irrep_generators)


class O2(O):
    def __init__(self):
        super().__init__()

        new_elems = []
        for g in self.elements:
            g.identifier["spinor"] = False
            new = copy.deepcopy(g)
            new.identifier['angle'] += 2*math.pi
            new.identifier['spinor'] = True
            new.rotation = util.rotation(
              new.identifier["direction"], new.identifier["angle"])
            if new.conjugacy_class not in ["C2xyz", "C2diag"]:
                new.conjugacy_class += 'bar'
            new_elems.append(new)

        for elem in new_elems:
            self.elements.append(elem)

        for g in self.elements:
            g.irreps["G1"] = util.g1_matrix(
              g.identifier["direction"], g.identifier["angle"])
            g.irreps["H"] = util.h_matrix(
              g.identifier["direction"], g.identifier["angle"])

            g.irreps["G2"] = g.irreps["G1"]

            if g.conjugacy_class in ["C4", "C4bar", "C2diag"]:
                g.irreps["A2"] = -g.irreps["A1"]
                g.irreps["T2"] = -g.irreps["T1"]
                g.irreps["G2"] = -g.irreps["G1"]

            g.rotation = g.irreps["T1"]


class Oh(O):
  def __init__(self):
    super().__init__()

    # add parity partner elements
    self.define_o_parity()
    self.add_parity_partners()

    self.rename_o_irreps()

    self.add_opposite_parity_irreps()

  def rename_o_irreps(self):
    for elem in self.elements:
      irreps = elem.irreps
      irreps["A1g"] = irreps.pop("A1")
      irreps["A2u"] = irreps.pop("A2")
      irreps["Eg"] = irreps.pop("E")
      irreps["T1u"] = irreps.pop("T1")
      irreps["T2g"] = irreps.pop("T2")

  def define_o_parity(self):
    for elem in self.elements:
      ids = elem.identifier
      ids["parity"] = 1

  def add_parity_partners(self):
    origin_elements = copy.deepcopy(self.elements)
    for elem in origin_elements:
      ids = elem.identifier
      ids["parity"] = -1

      parity_rotation = np.matmul(np.array(
        [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]), util.rotation(ids["direction"], ids["angle"]))

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
      parity = -1 if elem.conjugacy_class[0] == 'i' else 1
      irreps["A1u"] = parity*irreps["A1g"]
      irreps["A2g"] = parity*irreps["A2u"]
      irreps["Eu"] = parity*irreps["Eg"]
      irreps["T1g"] = parity*irreps["T1u"]
      irreps["T2u"] = parity*irreps["T2g"]


class O2h(O2):
  def __init__(self):
    super().__init__()

    # add parity partner elements
    self.define_o2_parity()
    self.add_parity_partners()
    self.rename_o2_irreps()
    self.add_opposite_parity_irreps()

  def define_o2_parity(self):
    for elem in self.elements:
      ids = elem.identifier
      ids["parity"] = 1

  def add_parity_partners(self):
    origin_elements = copy.deepcopy(self.elements)
    for elem in origin_elements:
      ids = elem.identifier
      ids["parity"] = -1

      parity_rotation = np.matmul(np.array([[-1,0,0],[0,-1,0],[0,0,-1]]),util.rotation(ids["direction"],ids["angle"]))

      g = util.GroupElement(
              ids,
              'i'+elem.conjugacy_class,
              parity_rotation,
              self.make_irreps(parity_rotation, self.irrep_generators)
          )
      g.irreps["G1"]=util.g1_matrix(g.identifier["direction"], g.identifier["angle"])
      g.irreps["H"]=util.h_matrix(g.identifier["direction"], g.identifier["angle"])

      g.irreps["G2"] = g.irreps["G1"]

      if g.conjugacy_class in ["C4", "C4bar", "C2diag", "iC4", "iC4bar", "iC2diag"]:
# self.make irreps correctly makes A2 and T2...
#          g.irreps["A2"] = -g.irreps["A1"]
#          g.irreps["T2"] = -g.irreps["T1"]
          g.irreps["G2"] = -g.irreps["G1"]

      self.elements.append(g)

  def rename_o2_irreps(self):
    for elem in self.elements:
      irreps = elem.irreps
      irreps["A1g"]=irreps.pop("A1")
      irreps["A2u"]=irreps.pop("A2")
      irreps["Eg"]=irreps.pop("E")
      irreps["T1u"]=irreps.pop("T1")
      irreps["T2g"]=irreps.pop("T2")
      irreps["G1g"]=irreps.pop("G1")
      irreps["G2g"]=irreps.pop("G2")
      irreps["Hg"]=irreps.pop("H")

  def add_opposite_parity_irreps(self):
    for elem in self.elements:
      irreps = elem.irreps
      parity = -1 if elem.conjugacy_class[0]=='i' else 1
      irreps["A1u"]=parity*irreps["A1g"]
      irreps["A2g"]=parity*irreps["A2u"]
      irreps["Eu"]=parity*irreps["Eg"]
      irreps["T1g"]=parity*irreps["T1u"]
      irreps["T2u"]=parity*irreps["T2g"]
      irreps["G1u"]=parity*irreps["G1g"]
      irreps["G2u"]=parity*irreps["G2g"]
      irreps["Hu"]=parity*irreps["Hg"]
