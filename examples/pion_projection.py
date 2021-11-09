from FiniteVolumeGroups.cubic import Oh 
import sympy as sp
import numpy as np

group = Oh()

# Sympy is an algebra package, and the variable names can now be used in equations.
pi = sp.Function('pion') 
parity = sp.Symbol('detR') # The parity of a rotation element R
char = sp.Symbol('chi') # the character of the group element under the irrep
mom = sp.MatrixSymbol('p',3,1) # The momentum of the pion
rot = sp.MatrixSymbol('R',3,3) # 3D rotation

# To project the pion onto different irreps we use the projection formula
# \pi^Lambda(p) = \sum_{g \in G} \chi_g^Lambda \det(R_g) \pi(R.p)


expr = pi(rot*mom) # this is how the pion's momentum rotates with element g

seed = char*parity*pi(rot*mom) # now add in pions parity(negative) and irrep character.
print('seed operator = {}\n'.format(seed)) 

# This is a seed with arbitrary momentum p
# Different momentum will go into different irreps in different ways

# lets just do two of the scalar irreps and p=[000].
for irrep in ['A1u','A1g']:
  tot = 0 # the final operator

  # sum over all group elements
  for elem in group.elements:
    # dictionary to substitute in values for symbols.
    values = {parity: elem.identifier['parity'], 
              mom: sp.Matrix([0,0,0]),
              rot: sp.Matrix(elem.irreps['T1u']),
              char: elem.irreps[irrep][0,0]} # will implement characters or trace function

    tot += seed.subs(values).doit()/len(group.elements)

  print('Projection of pion to {} = {}'.format(irrep,tot))

