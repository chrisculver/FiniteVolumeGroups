from FiniteVolumeGroups.elongated import *
from FiniteVolumeGroups.representation_checks import *


def test_d4():
    d4 = D4()
    assert len(d4.elements) == 8

    def class_elems(name): return sum(
        elem.conjugacy_class == name for elem in d4.elements)

    assert class_elems("E") == 1
    assert class_elems("C4z") == 2
    assert class_elems("C2z") == 1
    assert class_elems("C2xy") == 2
    assert class_elems("C2diag") == 2

    # some other quick checks
    print(d4.irrep("A1"))
    assert sum(d4.irrep("A1")) == 8
    assert sum(d4.irrep("A2")) == 0


def test_d4_characters():
    d4 = D4()

# http://symmetry.jacobs-university.de/cgi-bin/group.cgi?group=304&option=4
    a1_characters = {"E": 1, "C4z+": 1,   "C2z": 1,   "C2xy": 1,   "C2diag": 1}
    a2_characters = {"E": 1, "C4z+": 1,
                     "C2z": 1,   "C2xy": -1,  "C2diag": -1}
    b1_characters = {"E": 1, "C4z+": -1,
                     "C2z": 1,   "C2xy": 1,   "C2diag": -1}
    b2_characters = {"E": 1, "C4z+": -1,  "C2z": 1,   "C2xy": -1,  "C2diag": 1}
    e_characters = {"E": 2, "C4z+": 0,   "C2z": -2,  "C2xy": 0,   "C2diag": 0}

    all_characters = {"A1": a1_characters, "A2": a2_characters,
                      "B1": b1_characters, "B2": b2_characters,
                      "E": e_characters}

    def elements_of_class(name): return list(
        filter(lambda x: x.conjugacy_class == name, d4.elements))

    for irrep, characters in all_characters.items():
        for conj, char in characters.items():
            elems = elements_of_class(conj)
            for elem in elems:
                assert elem.irreps[irrep].trace() == char


def test_d4h():
    d4h = D4h()
    assert len(d4h.elements) == 16

    def class_elems(name): return sum(
        elem.conjugacy_class == name for elem in d4h.elements)

    assert class_elems("E") == 1
    assert class_elems("C4z") == 2
    assert class_elems("C2z") == 1
    assert class_elems("C2xy") == 2
    assert class_elems("C2diag") == 2
    assert class_elems("iE") == 1
    assert class_elems("iC4z") == 2
    assert class_elems("iC2z") == 1
    assert class_elems("iC2xy") == 2
    assert class_elems("iC2diag") == 2


def test_d4h_characters():
    d4h = D4h()

    a1g_characters = {"E": 1, "C4z+": 1,   "C2z": 1,   "C2xy": 1,   "C2diag": 1,
                      "iE": 1, "iC4z+": 1, "iC2z": 1,  "iC2xy": 1,  "iC2diag": 1}
    a2g_characters = {"E": 1, "C4z+": 1,   "C2z": 1,   "C2xy": -1,   "C2diag": -1,
                      "iE": 1, "iC4z+": 1, "iC2z": 1,  "iC2xy": -1,  "iC2diag": -1}
    b1g_characters = {"E": 1, "C4z+": -1,   "C2z": 1,   "C2xy": 1,   "C2diag": -1,
                      "iE": 1, "iC4z+": -1, "iC2z": 1,  "iC2xy": 1,  "iC2diag": -1}
    b2g_characters = {"E": 1, "C4z+": -1,   "C2z": 1,   "C2xy": -1,   "C2diag": 1,
                      "iE": 1, "iC4z+": -1, "iC2z": 1,  "iC2xy": -1,  "iC2diag": 1}
    eg_characters = {"E": 2, "C4z+": 0,   "C2z": -2,   "C2xy": 0,   "C2diag": 0,
                     "iE": 2, "iC4z+": 0, "iC2z": -2,  "iC2xy": 0,  "iC2diag": 0}
    a1u_characters = {"E": 1, "C4z+": 1,   "C2z": 1,   "C2xy": 1,   "C2diag": 1,
                      "iE": -1, "iC4z+": -1, "iC2z": -1,  "iC2xy": -1,  "iC2diag": -1}
    a2u_characters = {"E": 1, "C4z+": 1,   "C2z": 1,   "C2xy": -1,   "C2diag": -1,
                      "iE": -1, "iC4z+": -1, "iC2z": -1,  "iC2xy": 1,  "iC2diag": 1}
    b1u_characters = {"E": 1, "C4z+": -1,   "C2z": 1,   "C2xy": 1,   "C2diag": -1,
                      "iE": -1, "iC4z+": 1, "iC2z": -1,  "iC2xy": -1,  "iC2diag": 1}
    b2u_characters = {"E": 1, "C4z+": -1,   "C2z": 1,   "C2xy": -1,   "C2diag": 1,
                      "iE": -1, "iC4z+": 1, "iC2z": -1,  "iC2xy": 1,  "iC2diag": -1}
    eu_characters = {"E": 2, "C4z+": 0,   "C2z": -2,   "C2xy": 0,   "C2diag": 0,
                     "iE": -2, "iC4z+": 0, "iC2z": 2,  "iC2xy": 0,  "iC2diag": 0}

    all_characters = {"A1g": a1g_characters, "A2g": a2g_characters,
                      "B1g": b1g_characters, "B2g": b2g_characters,
                      "Eg": eg_characters,
                      "A1u": a1u_characters, "A2u": a2u_characters,
                      "B1u": b1u_characters, "B2u": b2u_characters,
                      "Eu": eu_characters}

    def elements_of_class(name): return list(
        filter(lambda x: x.conjugacy_class == name, d4h.elements))

    for irrep, characters in all_characters.items():
        for conj, char in characters.items():
            elems = elements_of_class(conj)
            for elem in elems:
                assert elem.irreps[irrep].trace() == char


def test_d4_reps():
  d4 = D4()
  for name, irrep in d4.elements[0].irreps.items():
    rep = [np.array(g.irreps[name], dtype=float) for g in d4.elements]
    assert(is_valid_rep(rep))


def test_d4h_reps():
  d4h = D4h()
  for name, irrep in d4h.elements[0].irreps.items():
    rep = [np.array(g.irreps[name], dtype=float) for g in d4h.elements]
    assert(is_valid_rep(rep))
