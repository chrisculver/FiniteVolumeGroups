Finite volume group base
========================
All concrete groups are derived from :py:class:`utilities.FiniteVolumeGroup`

Solving for irreps
==================
The file :code:`irrep.py` solves for the irreducible
representation :math:`I` of a group element by solving 

.. math::
   If(\vec{r})=f(g\vec{r})

where :math:`\vec{r}=(x,\,y,\,z)` is a vector, :math:`f` is a vector of functions left
invariant for the irrep(wording?), and :math:`g` is the three dimensional rep that rotates
a vector by the griven group element.


Concrete groups
===============

