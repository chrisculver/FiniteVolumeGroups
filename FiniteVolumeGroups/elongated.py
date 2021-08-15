import FiniteVolumeGroups.utilities as util
import numpy as np
import math
import copy

class D4(util.FiniteVolumeGroup):
    def __init__(self):
        element_generators = [
            util.ElementGenerator("E", 0., [ [0,0,1] ]),

            util.ElementGenerator("C4z", angle=math.pi/2.,
                directions = [ [0,0,1],  [0,0,-1] ]),

            util.ElementGenerator("C2z", math.pi, [ [0,0,1] ]),

            util.ElementGenerator("C2xy", angle=math.pi,
                directions = [ [1,0,0], [0,1,0] ]),

            util.ElementGenerator("C2diag", angle=math.pi,
                directions = [ [1,1,0], [-1,1,0] ])
        ]

        self.irrep_generators = {
            "A1": [lambda x,y,z: z*z],
            "A2": [lambda x,y,z: z],
            "B1": [lambda x,y,z: x*y*z],
            "B2": [lambda x,y,z: x*y],
            "E":  [lambda x,y,z: x, lambda x,y,z: y]
            }

        super().__init__(element_generators, self.irrep_generators)



class D4h(D4):
    def __init__(self):
        super().__init__();

        self.define_d4_parity()
        self.add_parity_partners()

        self.rename_d4_irreps()

        self.add_opposite_parity_irreps()

    def rename_d4_irreps(self):
        for elem in self.elements:
            irreps = elem.irreps
            irreps["A1g"]=irreps.pop("A1")
            irreps["A2u"]=irreps.pop("A2")
            irreps["B1u"]=irreps.pop("B1")
            irreps["B2g"]=irreps.pop("B2")
            irreps["Eu"]=irreps.pop("E")

    def define_d4_parity(self):
        for elem in self.elements:
            ids = elem.identifier
            ids["parity"] = 1

    def add_parity_partners(self):
        origin_elements = copy.deepcopy(self.elements)
        for elem in origin_elements:
            ids = elem.identifier
            ids["parity"] = -1

            parity_rotation=np.matmul(np.array([[-1,0,0],[0,-1,0],[0,0,-1]]),util.rotation(ids["direction"],ids["angle"]))

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
            irreps["B1g"]=parity*irreps["B1u"]
            irreps["B2u"]=parity*irreps["B2g"]
            irreps["Eg"]=parity*irreps["Eu"]
