import FiniteVolumeGroups as fvg

# Create the group Oh
oh = fvg.cubic.Oh()

# Get a group element, the first happens to be the identity
identity = oh.elements[0]
  
# How the group element rotates an object in 3-d space
print('I_{{3D}}={}\n'.format(identity.rotation))

# The irreps of the group
print('Irreps of Oh are {}\n'.format(identity.irreps.keys()))

# Get the rep matrix of an element in an irrep
irrep='A1g'
print('I_{{{}}}=\n{}\n'.format(irrep, identity(irrep)))

irrep='T1g'
print('I_{{{}}}=\n{}'.format(irrep, identity(irrep)))
