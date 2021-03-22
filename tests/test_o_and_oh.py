from src.cubic import *

def test_o():
  o = O()
  assert len(o.elements) == 24

  assert len(o.conjugacy_classes["E"]) == 1
  assert len(o.conjugacy_classes["C3"]) == 8
  assert len(o.conjugacy_classes["C2xyz"]) == 3 
  assert len(o.conjugacy_classes["C2diag"]) == 6 
  assert len(o.conjugacy_classes["C4"]) == 6 

def test_oh():
  oh = Oh()
  assert len(oh.elements) == 48
