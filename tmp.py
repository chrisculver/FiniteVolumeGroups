from FiniteVolumeGroups.cubic import *

o2 = O2()

for i,elem in enumerate(o2.elements):
    if elem.identifier["name"] in ["C4y", "C4z"] and elem.identifier["spinor"]==False:
        print("{} at index {}".format(elem.identifier["name"],i))

print(o2.elements[20].irreps["H"])

print(o2.elements[22].irreps["H"])

import math

math.pi/2

o2.elements[22].identifier

-1j*(math.pi/2)*1*np.array([[3./2.,0,0,0],[0,1./2.,0,0],[0,0,-1./2.,0],[0,0,0,-3./2.]])/2

math.sin(3*math.pi/4)
math.cos(3*math.pi/4)

3*math.pi/4

from scipy.linalg import expm
def h_matrix(r, phi):
    s32 = math.sqrt(3.)/2.
    spin32_generator = [ [[0,s32,0,0],[s32,0,1,0],[0,1,0,s32],[0,0,s32,0]],
                         [[0,-s32*1j,0,0],[s32*1j,0,-1j,0],[0,1j,0,-s32*1j],[0,0,s32*1j,0]],
                         [[3./2.,0,0,0],[0,1./2.,0,0],[0,0,-1./2.,0],[0,0,0,-3./2.]] ]

    norm_r = math.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])
    print(norm_r)
    arg = -1j*(np.asarray(phi*r[0])*spin32_generator[0]
            + np.asarray(phi*r[1])*spin32_generator[1]
            + np.asarray(phi*r[2])*spin32_generator[2])/(2.*norm_r)
    print(arg)
    tmp = expm( -1j*(np.asarray(phi*r[0])*spin32_generator[0]
            + np.asarray(phi*r[1])*spin32_generator[1]
            + np.asarray(phi*r[2])*spin32_generator[2])/(2.*norm_r) ).tolist()

    tmp = np.round(np.array(tmp),8)

    return tmp

h_matrix([0,0,1],math.pi/2)
