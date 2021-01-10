from distutils.core import setup
import setuptools

from pip._internal.req import parse_requirements


setup(
    name='iploader',
    version='1.1',
    packages=setuptools.find_packages(),
    long_description=open('README.md').read(),
    scripts= ['bin/iploader',],
)

