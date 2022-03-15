# README

This package constructs the elements and irreps of finite volume groups.  

## BASIC USAGE

To install the package in your python environment you can type 'pip install -e .'.
Then the following line should run 'import FiniteVolumeGroups as fvg'.

An example of the basic usage of the library is given in examples/basic_usage.py

For more advanced usage see finitevolumegroups.readthedocs.io

## TESTS
To run all the tests

    coverage run -m pytest
    coverage report -m

Checking that every irrep is valid is very time consuming...

The tests include
  1. Checks group has correct number of elements
  2. Checks each conjugacy class has the correct number of elements
  3. Check the character table for the group (character of the irrep for each conjugacy class)
  4. Check that each irrep is actual a rep of the group, i.e.
     a. closed
     b. associative
     c. has identity
     d. has inverse
     e. no rep elements are matrix of zeros.  

Note that step e was done so I don't have to solve for matrix inverses... but I have to
think about whether or not this is valid...
