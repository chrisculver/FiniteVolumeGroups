from FiniteVolumeGroups.cubic import *
from FiniteVolumeGroups.representation_checks import *


import math
import sys


def test_o2():
    o2 = O2()
    assert len(o2.elements) == 48

    def class_elems(name): return sum(
        elem.conjugacy_class == name for elem in o2.elements)

    assert class_elems("E") == 1
    assert class_elems("Ebar") == 1
    assert class_elems("C2xyz") == 6
    assert class_elems("C3") == 8
    assert class_elems("C3bar") == 8
    assert class_elems("C4") == 6
    assert class_elems("C4bar") == 6
    assert class_elems("C2diag") == 12


def test_o2h():
  o2h = O2h()
  assert(len(o2h.elements) == 96)

  def class_elems(name): return sum(
      elem.conjugacy_class == name for elem in o2h.elements)

  assert class_elems("E") == 1
  assert class_elems("Ebar") == 1
  assert class_elems("C2xyz") == 6
  assert class_elems("C3") == 8
  assert class_elems("C3bar") == 8
  assert class_elems("C4") == 6
  assert class_elems("C4bar") == 6
  assert class_elems("C2diag") == 12
  assert class_elems("iE") == 1
  assert class_elems("iEbar") == 1
  assert class_elems("iC2xyz") == 6
  assert class_elems("iC3") == 8
  assert class_elems("iC3bar") == 8
  assert class_elems("iC4") == 6
  assert class_elems("iC4bar") == 6
  assert class_elems("iC2diag") == 12


def test_o2_characters():
    o2 = O2()

    a1_characters = {"E":  1, "Ebar":  1,    "C2xyz":  1,     "C3":  1,
                     "C3bar":  1,   "C4":  1, "C4bar":  1, "C2diag":  1}
    a2_characters = {"E":  1, "Ebar":  1,    "C2xyz":  1,     "C3":  1,
                     "C3bar":  1,   "C4": -1, "C4bar": -1, "C2diag": -1}

    e_characters = {"E":  2, "Ebar":  2,    "C2xyz":  2,     "C3": -1,
                    "C3bar": -1,   "C4":  0, "C4bar":  0, "C2diag":  0}

    t1_characters = {"E":  3, "Ebar":  3,    "C2xyz": -1,     "C3":  0,
                     "C3bar":  0,   "C4":  1, "C4bar":  1, "C2diag": -1}
    t2_characters = {"E":  3, "Ebar":  3,    "C2xyz": -1,     "C3":  0,
                     "C3bar":  0,   "C4": -1, "C4bar": -1, "C2diag":  1}

    g1_characters = {"E":  2, "Ebar": -2,    "C2xyz":  0,     "C3":  1,
                     "C3bar": -1,   "C4":  math.sqrt(2), "C4bar": -math.sqrt(2), "C2diag": 0}
    g2_characters = {"E":  2, "Ebar": -2,    "C2xyz":  0,     "C3":  1,
                     "C3bar": -1,   "C4": -math.sqrt(2), "C4bar":  math.sqrt(2), "C2diag": 0}

    h_characters = {"E":  4, "Ebar": -4,    "C2xyz":  0,     "C3": -1,
                    "C3bar":  1,   "C4":   0, "C4bar":  0, "C2diag": 0}

    all_characters = {"A1": a1_characters, "A2": a2_characters,
                      "E": e_characters,
                      "T1": t1_characters, "T2": t2_characters,
                      "G1": g1_characters, "G2": g2_characters,
                      "H": h_characters}

    def elements_of_class(name): return list(
        filter(lambda x: x.conjugacy_class == name, o2.elements))

    for irrep, characters in all_characters.items():
      for conj, char in characters.items():
        elems = elements_of_class(conj)
        print("Irrep = {},  conj={}".format(irrep, conj))
        for elem in elems:
          print(elem.irreps[irrep])
          print(elem.identifier)
          print(char)
          print(elem.irreps[irrep].trace())
          trace = complex(elem.irreps[irrep].trace())
          assert np.isclose(trace.real, char)
          assert np.isclose(trace.imag, 0.)


def test_o2h_characters():
    o2h = O2h()
    #characters from arxiv 1706.00262 - copied from mathematica notebook
    a1g_characters = {"E": 1, "Ebar": 1, "C2xyz": 1, "C3": 1, "C3bar": 1,
                      "C4": 1, "C4bar": 1, "C2diag": 1, "iE": 1, "iEbar": 1, "iC2xyz": 1,
                      "iC3": 1, "iC3bar": 1, "iC4": 1, "iC4bar": 1, "iC2diag": 1}
    a2g_characters = {"E": 1, "Ebar": 1, "C2xyz": 1, "C3": 1, "C3bar": 1,
                      "C4": -1, "C4bar": -1, "C2diag": -1, "iE": 1, "iEbar": 1, "iC2xyz":
                      1, "iC3": 1, "iC3bar": 1, "iC4": -1, "iC4bar": -1, "iC2diag": -1}
    eg_characters = {"E": 2, "Ebar": 2, "C2xyz": 2, "C3": -1, "C3bar": -1,
                     "C4": 0, "C4bar": 0, "C2diag": 0, "iE": 2, "iEbar": 2, "iC2xyz": 2,
                     "iC3": -1, "iC3bar": -1, "iC4": 0, "iC4bar": 0, "iC2diag": 0}
    t1g_characters = {"E": 3, "Ebar": 3, "C2xyz": -1, "C3": 0, "C3bar": 0,
                      "C4": 1, "C4bar": 1, "C2diag": -1, "iE": 3, "iEbar": 3, "iC2xyz": -1,
                      "iC3": 0, "iC3bar": 0, "iC4": 1, "iC4bar": 1, "iC2diag": -1}
    t2g_characters = {"E": 3, "Ebar": 3, "C2xyz": -1, "C3": 0, "C3bar": 0,
                      "C4": -1, "C4bar": -1, "C2diag": 1, "iE": 3, "iEbar": 3, "iC2xyz":
                      -1, "iC3": 0, "iC3bar": 0, "iC4": -1, "iC4bar": -1, "iC2diag": 1}
    g1g_characters = {"E": 2, "Ebar": -2, "C2xyz": 0, "C3": 1, "C3bar": -1,
                      "C4": math.sqrt(2), "C4bar": -math.sqrt(2), "C2diag": 0, "iE": 2,
                      "iEbar": -2, "iC2xyz": 0, "iC3": 1, "iC3bar": -1, "iC4":
                      math.sqrt(2), "iC4bar": -math.sqrt(2), "iC2diag": 0}
    g2g_characters = {"E": 2, "Ebar": -2, "C2xyz": 0, "C3": 1, "C3bar": -1,
                      "C4": -math.sqrt(2), "C4bar": math.sqrt(2), "C2diag": 0, "iE": 2,
                      "iEbar": -2, "iC2xyz": 0, "iC3": 1, "iC3bar": -1, "iC4":
                      -math.sqrt(2), "iC4bar": math.sqrt(2), "iC2diag": 0}
    hg_characters = {"E": 4, "Ebar": -4, "C2xyz": 0, "C3": -1, "C3bar": 1,
                     "C4": 0, "C4bar": 0, "C2diag": 0, "iE": 4, "iEbar": -4, "iC2xyz": 0,
                     "iC3": -1, "iC3bar": 1, "iC4": 0, "iC4bar": 0, "iC2diag": 0}
    a1u_characters = {"E": 1, "Ebar": 1, "C2xyz": 1, "C3": 1, "C3bar": 1,
                      "C4": 1, "C4bar": 1, "C2diag": 1, "iE": -1, "iEbar": -1, "iC2xyz":
                      -1, "iC3": -1, "iC3bar": -1, "iC4": -1, "iC4bar": -1, "iC2diag": -1}
    a2u_characters = {"E": 1, "Ebar": 1, "C2xyz": 1, "C3": 1, "C3bar": 1,
                      "C4": -1, "C4bar": -1, "C2diag": -1, "iE": -1, "iEbar": -1, "iC2xyz":
                      -1, "iC3": -1, "iC3bar": -1, "iC4": 1, "iC4bar": 1, "iC2diag": 1}
    eu_characters = {"E": 2, "Ebar": 2, "C2xyz": 2, "C3": -1, "C3bar": -1,
                     "C4": 0, "C4bar": 0, "C2diag": 0, "iE": -2, "iEbar": -2, "iC2xyz":
                     -2, "iC3": 1, "iC3bar": 1, "iC4": 0, "iC4bar": 0, "iC2diag": 0}
    t1u_characters = {"E": 3, "Ebar": 3, "C2xyz": -1, "C3": 0, "C3bar": 0,
                      "C4": 1, "C4bar": 1, "C2diag": -1, "iE": -3, "iEbar": -3, "iC2xyz":
                      1, "iC3": 0, "iC3bar": 0, "iC4": -1, "iC4bar": -1, "iC2diag": 1}
    t2u_characters = {"E": 3, "Ebar": 3, "C2xyz": -1, "C3": 0, "C3bar": 0,
                      "C4": -1, "C4bar": -1, "C2diag": 1, "iE": -3, "iEbar": -3, "iC2xyz":
                      1, "iC3": 0, "iC3bar": 0, "iC4": 1, "iC4bar": 1, "iC2diag": -1}
    g1u_characters = {"E": 2, "Ebar": -2, "C2xyz": 0, "C3": 1, "C3bar": -1,
                      "C4": math.sqrt(2), "C4bar": -math.sqrt(2), "C2diag": 0, "iE": -2,
                      "iEbar": 2, "iC2xyz": 0, "iC3": -1, "iC3bar": 1, "iC4":
                      -math.sqrt(2), "iC4bar": math.sqrt(2), "iC2diag": 0}
    g2u_characters = {"E": 2, "Ebar": -2, "C2xyz": 0, "C3": 1, "C3bar": -1,
                      "C4": -math.sqrt(2), "C4bar": math.sqrt(2), "C2diag": 0, "iE": -2,
                      "iEbar": 2, "iC2xyz": 0, "iC3": -1, "iC3bar": 1, "iC4": math.sqrt(2),
                      "iC4bar": -math.sqrt(2), "iC2diag": 0}
    hu_characters = {"E": 4, "Ebar": -4, "C2xyz": 0, "C3": -1, "C3bar": 1,
                     "C4": 0, "C4bar": 0, "C2diag": 0, "iE": -4, "iEbar": 4, "iC2xyz": 0,
                     "iC3": 1, "iC3bar": -1, "iC4": 0, "iC4bar": 0, "iC2diag": 0}

    all_characters = {"A1g": a1g_characters, "A1u": a1u_characters,
                      "A2g": a2g_characters, "A2u": a2u_characters,
                      "Eg": eg_characters, "Eu": eu_characters,
                      "T1g": t1g_characters, "T1u": t1u_characters,
                      "T2g": t2g_characters, "T2u": t2u_characters,
                      "G1g": g1g_characters, "G1u": g1u_characters,
                      "G2g": g2g_characters, "G2u": g2u_characters,
                      "Hg": hg_characters, "Hu": hu_characters
                      }

    def elements_of_class(name): return list(
        filter(lambda x: x.conjugacy_class == name, o2h.elements))

    for irrep, characters in all_characters.items():
      for conj, char in characters.items():
        elems = elements_of_class(conj)
        print("Irrep = {},  conj={}".format(irrep, conj))
        for elem in elems:
          print(elem.irreps[irrep])
          print(elem.identifier)
          print("expected ", char)
          print("value ", elem.irreps[irrep].trace())
          trace = complex(elem.irreps[irrep].trace())
          assert np.isclose(trace.real, char)
          assert np.isclose(trace.imag, 0.)


def test_o2_reps():
  o2 = O2()
  for name, irrep in o2.elements[0].irreps.items():
    print("  testing for the {} irrep".format(name))
    rep = [np.array(g.irreps[name], dtype=complex) for g in o2.elements]
    assert(is_closed(rep))
    assert(is_associative(rep))
    assert(has_identity(rep))
    assert(has_inverses(rep))
    assert(is_nonzero(rep))


def test_o2h_reps():
  o2h = O2h()
  for name, irrep in o2h.elements[0].irreps.items():
    print("  testing for the {} irrep".format(name))
    rep = [np.array(g.irreps[name], dtype=complex) for g in o2h.elements]
    assert(is_closed(rep))
    assert(is_associative(rep))
    assert(has_identity(rep))
    assert(has_inverses(rep))
    assert(is_nonzero(rep))
