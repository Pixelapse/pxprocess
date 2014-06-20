#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

setup(
  name='process',
  version='0.0.1dev',
  packages=find_packages(),
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
