Group generation
================

Finite volume group base
------------------------
All concrete groups are derived from :py:class:`utilities.FiniteVolumeGroup`.  This 
abstract class computes the irreps and 3D representation for each group element.  
It requires that the elements are given by conjugacy classes, for which there is one
angle of rotation but multiple axis around which the rotation happens.  The irreps
are generated according to the functions that are left invariant by the rotations. 
The functions are passed as a list of lambda functions.  

Groups with parity
----------------------
To extend a group to include parity rotations, we first add the parity partner to all
group elements by composing an inversion with the 3D rotation.  Then we rename
the existing irreps to include the new parity labels.  The "old" irreps are NOT all 
positive parity irreps.  To get the remaining irreps for each group element we take
the existing irrep and multiply it by the determing of the group elements 3d representation.
This multiplies the irrep by :math:`\pm 1`.



Solving for irreps
------------------
The file :code:`irrep.py` solves for the irreducible
representation :math:`I` of a group element by solving 

.. math::
   If(\vec{r})=f(g\vec{r})

where :math:`\vec{r}=(x,\,y,\,z)` is a vector, :math:`f` is a vector of functions left
invariant for the irrep(wording?), and :math:`g` is the three dimensional rep that rotates
a vector by the griven group element.


Concrete groups
---------------
To create groups using the above, we need to specify the parameters we need to generate the 
group elements, and to specify the functions that are invariant under different irreps.

The group element rotation angles and directions are from Phys. Rev. D 96, 054508 (2017).

The irrep functions are from symmetry.jacobs-university.de, on the appropriate webpage.
