
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
