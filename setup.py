# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='1.0.0',
    description='Get COVID data from an API',
    long_description=readme,
    author='Harry Shyket',
    author_email='',
    url='https://github.com/hs2323/covid-data',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

