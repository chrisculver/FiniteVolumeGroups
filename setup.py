from setuptools import setup

setup(
  name='FiniteVolumeGroups',
  version='0.1.0',
  author='Chris Culver',
  packages=['FiniteVolumeGroups'],
  license='LICENSE.txt',
  description='Package for setting up finite volume groups',
  long_description=open('README.md').read(),
  install_requires=open('requirements.py').read()
    )
