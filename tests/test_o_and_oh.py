from FiniteVolumeGroups.cubic import *
from FiniteVolumeGroups.representation_checks import *


def test_o():
  o = O()
  assert len(o.elements) == 24

  def class_elems(name): return sum(
    elem.conjugacy_class == name for elem in o.elements)

  assert class_elems("E") == 1
  assert class_elems("C3") == 8
  assert class_elems("C2xyz") == 3
  assert class_elems("C2diag") == 6
  assert class_elems("C4") == 6


def test_o_irreps():
  o = O()

  # some quick character checks
  assert sum(o.irrep("A1")) == 24
  assert sum(o.irrep("A2")) == 0


def test_o_characters():
  o = O()

  # http://symmetry.jacobs-university.de/cgi-bin/group.cgi?group=903&option=4
  a1_characters = {"E": 1, "C3":  1, "C2diag":  1, "C4":  1, "C2xyz":  1}
  a2_characters = {"E": 1, "C3":  1, "C2diag": -1, "C4": -1, "C2xyz":  1}
  e_characters = {"E": 2, "C3": -1, "C2diag":  0, "C4":  0, "C2xyz":  2}
  t1_characters = {"E": 3, "C3":  0, "C2diag": -1, "C4":  1, "C2xyz": -1}
  t2_characters = {"E": 3, "C3":  0, "C2diag":  1, "C4": -1, "C2xyz": -1}

  all_characters = {"A1": a1_characters, "A2": a2_characters,
                    "E": e_characters,
                    "T1": t1_characters, "T2": t2_characters}

  def elements_of_class(name): return list(
    filter(lambda x: x.conjugacy_class == name, o.elements))

  for irrep, characters in all_characters.items():
    for conj, char in characters.items():
      elems = elements_of_class(conj)
      for elem in elems:
        assert elem.irreps[irrep].trace() == char


def test_oh():
  oh = Oh()
  assert len(oh.elements) == 48

  def class_elems(name): return sum(
    elem.conjugacy_class == name for elem in oh.elements)

  assert class_elems("E") == 1
  assert class_elems("C3") == 8
  assert class_elems("C2xyz") == 3
  assert class_elems("C2diag") == 6
  assert class_elems("C4") == 6
  assert class_elems("iE") == 1
  assert class_elems("iC3") == 8
  assert class_elems("iC2xyz") == 3
  assert class_elems("iC2diag") == 6
  assert class_elems("iC4") == 6


def test_oh_characters():
  oh = Oh()

  # From http://symmetry.jacobs-university.de/cgi-bin/group.cgi?group=904&option=4
  # in the same order.  The definitinos for S and sigma are in
  # https://www.theochem.ru.nl/files/local/altmann-2011.pdf - page 25.

  A1g_characters = {"E":  1,  "C3":  1,  "C2diag":  1,     "C4":  1,   "C2xyz":  1,
                    "iE":  1, "iC4":  1,     "iC3":  1, "iC2xyz":  1, "iC2diag":  1}
  A2g_characters = {"E":  1,  "C3":  1,  "C2diag": -1,     "C4": -1,   "C2xyz":  1,
                    "iE":  1, "iC4": -1,     "iC3":  1, "iC2xyz":  1, "iC2diag": -1}
  Eg_characters = {"E":  2,  "C3": -1,  "C2diag":  0,     "C4":  0,   "C2xyz":  2,
                   "iE":  2, "iC4":  0,     "iC3": -1, "iC2xyz":  2, "iC2diag":  0}
  T1g_characters = {"E":  3,  "C3":  0,  "C2diag": -1,     "C4":  1,   "C2xyz": -1,
                    "iE":  3, "iC4":  1,     "iC3":  0, "iC2xyz": -1, "iC2diag": -1}
  T2g_characters = {"E":  3,  "C3":  0,  "C2diag":  1,     "C4": -1,   "C2xyz": -1,
                    "iE":  3, "iC4": -1,     "iC3":  0, "iC2xyz": -1, "iC2diag":  1}

  A1u_characters = {"E":  1,  "C3":  1,  "C2diag":  1,     "C4":  1,   "C2xyz":  1,
                    "iE": -1, "iC4": -1,     "iC3": -1, "iC2xyz": -1, "iC2diag": -1}
  A2u_characters = {"E":  1,  "C3":  1,  "C2diag": -1,     "C4": -1,   "C2xyz":  1,
                    "iE": -1, "iC4":  1,     "iC3": -1, "iC2xyz": -1, "iC2diag":  1}
  Eu_characters = {"E":  2,  "C3": -1,  "C2diag":  0,     "C4":  0,   "C2xyz":  2,
                   "iE": -2, "iC4":  0,     "iC3":  1, "iC2xyz": -2, "iC2diag":  0}
  T1u_characters = {"E":  3,  "C3":  0,  "C2diag": -1,     "C4":  1,   "C2xyz": -1,
                    "iE": -3, "iC4": -1,     "iC3":  0, "iC2xyz":  1, "iC2diag":  1}
  T2u_characters = {"E":  3,  "C3":  0,  "C2diag":  1,     "C4": -1,   "C2xyz": -1,
                    "iE": -3, "iC4":  1,     "iC3":  0, "iC2xyz":  1, "iC2diag": -1}

  all_characters = {"A1g": A1g_characters, "A2g": A2g_characters,
                    "Eg": Eg_characters,
                    "T1g": T1g_characters, "T2g": T2g_characters,
                    "A1u": A1u_characters, "A2u": A2u_characters,
                    "Eu": Eu_characters,
                    "T1u": T1u_characters, "T2u": T2u_characters}

  def elements_of_class(name): return list(
    filter(lambda x: x.conjugacy_class == name, oh.elements))

  for irrep, characters in all_characters.items():
    for conj, char in characters.items():
      elems = elements_of_class(conj)
      for elem in elems:
        assert elem.irreps[irrep].trace() == char


def test_o_reps():
  o = O()
  for name, irrep in o.elements[0].irreps.items():
    rep = [np.array(g.irreps[name], dtype=float) for g in o.elements]
    assert(is_closed(rep))
    assert(is_associative(rep))
    assert(has_identity(rep))
    assert(has_inverses(rep))
    assert(is_nonzero(rep))


def test_oh_reps():
  oh = Oh()
  for name, irrep in oh.elements[0].irreps.items():
    rep = [np.array(g.irreps[name], dtype=float) for g in oh.elements]
    assert(is_closed(rep))
    assert(is_associative(rep))
    assert(has_identity(rep))
    assert(has_inverses(rep))
    assert(is_nonzero(rep))
