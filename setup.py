#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

import process

setup(
  name='process',
  version=process.__version__,
  packages=find_packages(),
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
