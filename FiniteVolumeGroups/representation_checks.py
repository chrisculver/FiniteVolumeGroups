import numpy as np


def is_valid_rep(rep):
  res = True
  if not has_identity(rep):
    res = False
  if not is_closed(rep):
    res = False
  if not has_inverses(rep):
    res = False
  if not is_associative(rep):
    res = False

  return res


def is_closed(rep):
  res = True
  for i1, g1 in enumerate(rep):
      for i2, g2 in enumerate(rep):
          prod = np.matmul(g1, g2)
          if not any(np.allclose(prod, g) for g in rep):
              res = False
              raise AssertionError(
                "rep not closed for elem indices {} {}".format(i1, i2))
  return res


def is_associative(rep):
  res = True
  for i1, a in enumerate(rep):
      for i2, b in enumerate(rep):
          for i3, c in enumerate(rep):
              lhs = np.matmul(np.matmul(a, b), c)
              rhs = np.matmul(a, np.matmul(b, c))
              if not np.allclose(lhs, rhs):
                  res = False
                  raise AssertionError(
                    "rep not associative for elem indices {} {} {}".format(i1, i2, i3))
  return res


def has_identity(rep):
  res = False
  id = np.identity(len(rep[0]))
  for g in rep:
    if np.allclose(g, id):
      res = True
  if not res:
    raise AssertionError("rep doesn't have identity")
  return res


def has_inverses(rep):
  res = True
  for i1, g1 in enumerate(rep):
      has_inverse = False
      for i2, g2 in enumerate(rep):
          if np.allclose(np.matmul(g1, g2), np.identity(len(rep[0]))):
              has_inverse = True
      if not has_inverse:
          res = False
          raise AssertionError("rep missing inverse for element {}".format(i1))
  return res
