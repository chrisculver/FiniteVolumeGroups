import sympy as sp
import numpy as np

# solve irrep.funcs(x,y,z) == funcs(elem.(x,y,z))
# return irrep
def generate_irrep(elem, funcs):                                                                                      
    dim = len(funcs) # of the irrep                                                                                     
    #print(dim)
    a = [ sp.symbols('a'+str(i)) for i in range(dim*dim) ] # symbols needed for irrep  
    (x,y,z) = sp.symbols('x, y, z')
    (xp,yp,zp) = elem*np.matrix([[x],[y],[z]])
    xp=xp[0,0]
    yp=yp[0,0]
    zp=zp[0,0]
    
    irrep = np.matrix([[ a[i*dim + j] for i in range(dim) ] for j in range(dim) ])
    func_vec = np.matrix([ [funcs[i](x,y,z)] for i in range(dim) ])
    
    func_rotated_vec = np.matrix([ [funcs[i](xp,yp,zp)] for i in range(dim) ])

    equations = np.asarray(irrep*func_vec - func_rotated_vec).flatten()
    #print(equations)
    equations = [sp.expand(eq) for eq in equations]
    #print(equations)
    
    coefficient_equations = []
    for eq in equations:
        for i in range(1,4):
            varx = x**i
            vary = y**i
            varz = z**i
            coefficient_equations.append( eq.coeff(varx))
            coefficient_equations.append( eq.coeff(vary))
            coefficient_equations.append( eq.coeff(varz))
        
    #print(coefficient_equations)
    
    #print(sp.linsolve(coefficient_equations, *a))
    
    solution = sp.linsolve(coefficient_equations, *a).args
    
    #print(solution)
    
    return np.matrix([[ solution[0][i*dim+j] for i in range(dim)] for j in range(dim)]) 





