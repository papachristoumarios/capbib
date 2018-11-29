import setuptools
from setuptools import setup, find_packages

setup(
    name='capbib',
    version='1.0',
    description='Capbib : Bibliography Transformations made easier',
    author='Marios Papachristou',
    author_email='papachristoumarios@gmail.com',
    url='https://github.com/papachristoumarios/capbib',
    packages=['capbib'],
    package_dir={'capbib': 'capbib'},
    scripts=['capbib/capbib.py'])
