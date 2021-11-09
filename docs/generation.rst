Group generation
================

Finite volume group base
------------------------
All concrete groups are derived from :py:class:`utilities.FiniteVolumeGroup`.  This abstract class computes the irreps and 3D representation for each group element.  The 3D representation is generated using the generators of :math:`SO(3)`, called :math:`\vec{\tau}`.  Given a normalized direction :math:`\vec{r}` and angle of rotation :math:`\phi`, the 3D representation is

.. math::
   R_{\text{3D}}=e^{\phi \vec{r}.\vec{\tau}}.

To see how the irreps are generated given the 3D representation see `Solving for irreps`_ below.

Solving for irreps
------------------
The file :code:`irrep.py` solves for the irreducible
representation :math:`I` of a group element by solving 

.. math::
   If(\vec{r})=f(g\vec{r})

where :math:`\vec{r}=(x,\,y,\,z)` is a vector, :math:`f` is a vector of functions
invariant under the irrep, and :math:`g` is the three dimensional rep that rotates
a vector by the griven group element.

Groups with parity
----------------------
To extend a group to include, we first add the parity partner of all
group elements by composing an inversion with the 3D rotation of that group element.  Then we rename
the existing irreps to include parity labels.  Note that the old irreps are *NOT* 
necessarily positive parity irreps as one might think.  To get the remaining irreps for each group element we take
the existing irrep and multiply it by the determining of the group elements 3D representation.
This multiplies the irrep by :math:`\pm 1`, and gives the irrep the opposite parity.  

Concrete groups
---------------
To create groups using the above, we need to specify the parameters we need to generate the 
group elements, and to specify the functions that are invariant under different irreps.

The group element rotation angles and directions are from Phys. Rev. D 96, 054508 (2017).

The irrep functions are from symmetry.jacobs-university.de, on the appropriate webpage.
