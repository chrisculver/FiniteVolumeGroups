.. Finite Volume Gruops documentation master file, created by
   sphinx-quickstart on Fri Jan 22 16:11:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Finite Volume Groups
====================

This package constructs the finite-volume rotation groups, from a list of
angles and directions about which the rotation occurs in 3D space.  It also
constructs the irrep matrix for each group element and irrep of the group.  For
basic usage see basic_usage.py_.  To see how one might project a LQCD
operator to a specific irrep with Sympy_ see pion_projection.py_.

.. _basic_usage.py: https://github.com/chrisculver/FiniteVolumeGroups/blob/main/examples/basic_usage.py
   
.. _Sympy: https://www.sympy.org

.. _pion_projection.py: https://github.com/chrisculver/FiniteVolumeGroups/blob/main/examples/pion_projection.py


The code is organized into two types of files.  The concrete implementations of classed are 
defined in :code:`cubic.py` and :code:`elongated.py`, which define the classes for the
groups :math:`O, O_h, D_4, D_{4h}`.  The other files contain utility functions to generate 
any finite-volume group from some defining information.  A more detailed description is
given in :doc:`generation`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   generation

.. toctree::
   :maxdepth: 2
   :caption: API: 

   groupElement
   finiteVolumeGroup
