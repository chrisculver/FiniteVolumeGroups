from src.cubic import *

def test_o():
  o = O()
  assert len(o.elements) == 24

def test_oh():
  oh = Oh()
  assert len(oh.elements) == 48
