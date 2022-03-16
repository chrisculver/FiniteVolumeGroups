import numpy as np


def is_valid_rep(rep):
  res = True
  if not is_closed(rep):
    res = False
  if not is_associative(rep):
    res = False
  if not is_nonzero(rep):
    res = False
  if not has_identity(rep):
    res = False
  if not has_inverses(rep):
    res = False

  return res


def is_closed(rep):
  res = True
  for g1 in rep:
      for g2 in rep:
          prod = np.matmul(g1, g2)
          if not any(np.allclose(prod, g) for g in rep):
              res = False
  return res


def is_associative(rep):
  res = True
  for a in rep:
      for b in rep:
          for c in rep:
              lhs = np.matmul(np.matmul(a, b), c)
              rhs = np.matmul(a, np.matmul(b, c))
              if not np.allclose(lhs, rhs):
                  res = False
  return res


def has_identity(rep):
  res = False
  id = np.identity(len(rep[0]))
  for g in rep:
    if np.allclose(g, id):
      res = True
  return res


def has_inverses(rep):
  res = True
  for g1 in rep:
      has_inverse = False
      for g2 in rep:
          if np.allclose(np.matmul(g1, g2), np.identity(len(rep[0]))):
              has_inverse = True
      if not has_inverse:
          res = False
  return res


def is_nonzero(rep):
  res = True
  zero = np.zeros((len(rep[0]), len(rep[0])))
  for g in rep:
    if np.allclose(g, zero):
      res = False
  return res
