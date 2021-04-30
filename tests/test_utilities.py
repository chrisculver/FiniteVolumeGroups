from FiniteVolumeGroups.utilities import *
from pytest import approx
import math

# because floating points
def assertMatricesAlmostEqual(x,y):
  assert len(x) == len(y)
  assert len(x[0]) == len(y[0])
  for i in range(len(x)):
    for j in range(len(y)):
      assert x[i][j] == approx(y[i][j])


def test_matmul():
  x = [[1,2,0],[3,1,2],[0,0,4]]
  y = [[2,0,0],[1,0,1],[1,1,1]]

  assert matmul(x,y) == [[4,0,2],[9,2,3],[4,4,4]]


def test_rotations():
  assertMatricesAlmostEqual(
                              [[1.,0.,0.],[0.,-1.,0.],[0.,0.,-1.]],
                              rotation([1.,0.,0.],math.pi)
                           )

  assert [[1,0,0],[0,-1,0],[0,0,-1]] == rotation([1,0,0],math.pi)

def test_generate_closed_elements():
  id_mat = [[1,0,0],[0,1,0],[0,0,1]]
  elements = generate_closed_elements([id_mat])

  assert elements == [ id_mat ]
  
