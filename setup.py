from distutils.core import setup

from pip._internal.req import parse_requirements

reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', session='hack')]

setup(
    name='iploader',
    version='RC-0.1',
    packages=['iploader',],
    license='GPL3',
    long_description=open('README.md').read(),
    scripts= ['bin/iploader',],
    install_requires= reqs
)

