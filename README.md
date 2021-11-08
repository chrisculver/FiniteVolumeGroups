# README

This package constructs the elements and irreps of finite volume groups.  

## BASIC USAGE

To install the package in your python environment you can type 'pip install -e .'. 
Then the following line should run 'import FiniteVolumeGroups as fvg'.

How to access some of the most common data is provided in the following:

```
  import FiniteVolumeGroups as fvg
  oh = fvg.cubic.Oh()
  # Get a group element, the first happens to be the identity
  identity = oh.elements[0]
  
  # How the group element rotates an object in 3-d space
  print(identity.rotation)

  # The irreps of the group
  print(identity.irreps.keys())

  # Get the rep matrix of an element in an irrep
  irrep='A1g'
  print(identity(irrep))
  
```

For more advanced usage see finitevolumegroups.readthedocs.io

## TESTS
To run all the tests 

    coverage run -m pytest
    coverage report -m 


## TODO
1. Does O2h also have integer matrix elements
2. C4v
