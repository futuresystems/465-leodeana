#!/usr/bin/env python

version = "1.0"


requirements = [
    'future',
    'sh',
    'docopt',
    'pyaml',
    'simplejson',
    'nose',
    'python-hostlist',
    'prettytable',
    'pytimeparse',
    ]

from setuptools import setup, find_packages
from setuptools.command.install import install
import glob
import os

package_name = "cloudmesh_uebercool"

try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import auto_create_version
from cloudmesh_base.util import auto_create_requirements


banner("Installing Cloudmesh " + package_name)

home = os.path.expanduser("~")

auto_create_version(package_name, version)
auto_create_requirements(requirements)


class UploadToPypi(install):
    """Upload the package to pypi."""
    def run(self):
        os.system("Make clean Install")
        os.system("python setup.py.in install")
        banner("Build Distribution")
        os.system("python setup.py.in sdist --format=bztar,zip upload")


class RegisterWithPypi(install):
    """Upload the package to pypi."""
    def run(self):
        banner("Register with Pypi")
        os.system("python setup.py.in register")


class InstallBase(install):
    """Install the package."""
    def run(self):
        banner("Installing Cloudmesh " + package_name)
        install.run(self)


class InstallRequirements(install):
    """Install the requirements."""
    def run(self):
        banner("Installing Requirements for Cloudmesh " + package_name)
        os.system("pip install -r requirements.txt")


class InstallAll(install):
    """Install requirements and the package."""
    def run(self):
        banner("Installing Requirements for Cloudmesh " + package_name)
        os.system("pip install -r requirements.txt")
        banner("Installing Cloudmesh " + package_name)
        install.run(self)

setup(
    name='MODULE',
    version=version,
    description='A set of simple base functions and classes useful for cloudmesh and other programs',
    # description-file =
    #    README.rst
    author='The Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/base',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    install_requires=requirements,
    cmdclass={
        'install': InstallBase,
        'requirements': InstallRequirements,
        'all': InstallAll,
        'pypi': UploadToPypi,
        'pypiregister': RegisterWithPypi,
        },
)

