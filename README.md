# README

This package constructs the finite-volume groups and irreps useful for lattice QCD calculations.



## TESTS
It's important we have a set of rigorous tests, since the results are very
well known, and we want this to be a black box after development. Anybody
looking through the tests should really be confident that these are valid 
tests. 

To run all the tests 

    coverage run -m pytest
    coverage report -m 


## TODO
1. Irreps
2. More tests
3. Test character table using conjugacy classes for all irreps using
symmetry.jacobs-university.de
4. Does O2h also have integer matrix elements
