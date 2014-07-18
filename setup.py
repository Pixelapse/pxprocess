#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

version = '0.0.2'

setup(
  name='pxprocess',
  version=version,
  url='http://github.com/Pixelapse/pxprocess',
  download_url='https://github.com/Pixelapse/pxprocess/tarball/v%s' % version,
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  maintainer='Pixelapse',
  maintainer_email='hello@pixelapse.com',
  packages=find_packages(),
  description='Friendly replacement for subprocess',
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
