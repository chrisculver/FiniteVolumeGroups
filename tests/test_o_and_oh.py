from src.cubic import *

def test_o():
  o = O()
  assert len(o.elements) == 24

  class_elems = lambda name : sum(elem.conjugacy_class == name for elem in o.elements) 
  
  assert class_elems("E") == 1
  assert class_elems("C3") == 8
  assert class_elems("C2xyz") == 3 
  assert class_elems("C2diag") == 6 
  assert class_elems("C4") == 6 


def test_o_irreps():
  o = O()

  irrep = lambda name : [ elem.irreps[name] for elem in o.elements]

  # some quick checks
  assert sum(irrep("A1")) == 24
  assert sum(irrep("A2")) == 0

 


#def test_oh():
#  oh = Oh()
#  assert len(oh.elements) == 48
