from src.cubic import Oh 
import sympy as sp
import numpy as np

group = Oh()

pi = sp.Function('f')
parity = sp.Symbol('detR')
char = sp.Symbol('chi')
mom = sp.MatrixSymbol('p',3,1)
rot = sp.MatrixSymbol('R',3,3)

expr = pi(rot*mom)

seed = char*parity*pi(rot*mom)

for irrep in ['A1u','A1g']:
  tot = 0
  for elem in group.elements:
    values = {parity: elem.identifier['parity'], 
              mom: sp.Matrix([0,0,0]),
              rot: elem.irreps['T1u'],
              char: elem.irreps[irrep][0,0]} # will implement characters or trace function
    tot += seed.subs(values).doit()

  print('Projection of pion to ' + irrep + ' = ' + str(tot))


#U(g) O U(g)^T
#O = rho * pi * sigma (p)

#vector part under t1u -> g['t1g'].vec
#pseduscalar part under a1u -> g.parity() 
#scalar part under a1g -> +1

#O_i = rho_i * pi * sigma
#| g['t1g'].i,  g.parity()*pi,  sigma> 
#U(g) | i , pi, sigma > = | g['t1g'].i,  g.parity()*pi,  sigma> 

#rho_{alpha, beta, i} = Phi^{du}_alpha,beta,i

#O -> g['t1g'].rho * g.parity()*pi * +1 * sigma ( g['t1g'].p ) 

#T3 = < p | X + Y + Z | q > 
#T3 -> < g['t1g'].vec | (X + Y + Z) | g['t1g'].vec, l, m> 
#U(g) -> 




