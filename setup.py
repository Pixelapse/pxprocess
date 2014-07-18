#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

setup(
  name='process',
  version='0.0.1',
  url='http://github.com/Pixelapse/process',
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  maintainer='Pixelapse',
  maintainer_email='hello@pixelapse.com',
  packages=find_packages(),
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
