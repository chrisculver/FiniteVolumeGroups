import sympy as sp
import numpy as np

# solve irrep.funcs(x,y,z) == funcs(elem.(x,y,z))
# return irrep
def generate_irrep(elem, funcs):                                                                                      
    dim = len(funcs) # of the irrep                                                                                     
    #print(dim)
    a = [ sp.symbols('a'+str(i)) for i in range(dim*dim) ] # symbols needed for irrep  
    (x,y,z) = sp.symbols('x, y, z')
#    print(elem)
#    print(np.array([x,y,z]))
#    print(np.matmul(np.array(elem),np.array([x,y,z])))
    (xp,yp,zp) = np.matmul(np.array(elem),np.array([x,y,z]))
   
#    print(xp)
#    print(yp)
#    print(zp)

    irrep = np.array([[ a[i*dim + j] for i in range(dim) ] for j in range(dim) ])
    func_vec = np.array([ [funcs[i](x,y,z)] for i in range(dim) ])
    
#    print(irrep)
#    print(func_vec)
    func_rotated_vec = np.array([ [funcs[i](xp,yp,zp)] for i in range(dim) ])
#    print(func_rotated_vec)

    equations = np.asarray(np.matmul(irrep,func_vec) - func_rotated_vec).flatten()
#    print(equations)
    equations = [sp.expand(eq) for eq in equations]
#    print(equations)
    
    coefficient_equations = []
    for eq in equations:
        for i in range(1,4):
            varx = x**i
            vary = y**i
            varz = z**i
            coefficient_equations.append( eq.coeff(varx))
            coefficient_equations.append( eq.coeff(vary))
            coefficient_equations.append( eq.coeff(varz))
        
#    print(coefficient_equations)   
#    print(sp.linsolve(coefficient_equations, *a))
    
    solution = sp.linsolve(coefficient_equations, *a).args
    
#    print(solution)
    
    return np.array([[ solution[0][i*dim+j] for i in range(dim)] for j in range(dim)]) 





