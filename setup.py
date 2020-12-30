from distutils.core import setup
import setuptools

from pip._internal.req import parse_requirements

reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', session='hack')]

setup(
    name='iploader',
    version='RC-0.1',
    packages=setuptools.find_packages(),
    long_description=open('README.md').read(),
    scripts= ['bin/iploader',],
    install_requires= reqs
)

