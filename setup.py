#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='drf-simple-api-key-auth',
    version='0.1.0',
    description='Simple API key auth for Django REST Framework',
    author='Art Processors',
    author_email='jacob@artprocessors.net',
    url='https://github.com/ArtProcessors/drf-simple-api-key-auth',
    packages=find_packages(),
    install_requires=['django']
)
