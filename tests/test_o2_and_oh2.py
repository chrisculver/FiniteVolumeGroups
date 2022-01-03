from FiniteVolumeGroups.cubic import *

import math
import sys

def test_o2():
    o2 = O2()
    assert len(o2.elements) == 48

    class_elems = lambda name : sum(elem.conjugacy_class == name for elem in o2.elements)

    assert class_elems("E") == 1
    assert class_elems("Ebar") == 1
    assert class_elems("C2xyz") == 6
    assert class_elems("C3") == 8
    assert class_elems("C3bar") == 8
    assert class_elems("C4") == 6
    assert class_elems("C4bar") == 6
    assert class_elems("C2diag") == 12


def test_o2_characters():
    o2 = O2()

    a1_characters = {    "E":  1, "Ebar":  1,    "C2xyz":  1,     "C3":  1,
                     "C3bar":  1,   "C4":  1, "C4bar":  1, "C2diag":  1}
    a2_characters = {    "E":  1, "Ebar":  1,    "C2xyz":  1,     "C3":  1,
                     "C3bar":  1,   "C4": -1, "C4bar": -1, "C2diag": -1}

    e_characters =  {    "E":  2, "Ebar":  2,    "C2xyz":  2,     "C3": -1,
                     "C3bar": -1,   "C4":  0, "C4bar":  0, "C2diag":  0}

    t1_characters = {    "E":  3, "Ebar":  3,    "C2xyz": -1,     "C3":  0,
                     "C3bar":  0,   "C4":  1, "C4bar":  1, "C2diag": -1}
    t2_characters = {    "E":  3, "Ebar":  3,    "C2xyz": -1,     "C3":  0,
                     "C3bar":  0,   "C4": -1, "C4bar": -1, "C2diag":  1}

    g1_characters = {    "E":  2, "Ebar":  -2,    "C2xyz":  0,     "C3":  1,
                     "C3bar":  -1,   "C4":  math.sqrt(2), "C4bar":  -math.sqrt(2), "C2diag": 0}
    g2_characters = {    "E":  2, "Ebar":  -2,    "C2xyz":  0,     "C3":  1,
                     "C3bar":  -1,   "C4": -math.sqrt(2), "C4bar":  math.sqrt(2), "C2diag": 0}

    h_characters =  {    "E":  4, "Ebar":  -4,    "C2xyz":  0,     "C3": -1,
                     "C3bar":  1,   "C4":   0, "C4bar":  0, "C2diag": 0}

    all_characters = {"A1": a1_characters, "A2": a2_characters,
                      "E": e_characters,
                      "T1": t1_characters, "T2": t2_characters,
                      "G1": g1_characters, "G2": g2_characters,
                      "H": h_characters}


    elements_of_class = lambda name: list(filter(lambda x: x.conjugacy_class == name, o2.elements))

    for irrep, characters in all_characters.items():
      for conj, char in characters.items():
        elems = elements_of_class(conj)
        print("Irrep = {},  conj={}".format(irrep,conj))
        for elem in elems:
          print(elem.irreps[irrep])
          print(elem.identifier)
          print(char)
          print(elem.irreps[irrep].trace())
          trace=complex(elem.irreps[irrep].trace())
          assert np.isclose(trace.real, char)
          assert np.isclose(trace.imag, 0.)
