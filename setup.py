#!/usr/bin/env python
# encoding: utf-8
"""
setup.py
"""

from setuptools import setup, find_packages
import os

execfile(os.path.join('sforce', 'version.py'))

setup(
    name = 'sforce',
    version = VERSION,
    description = 'Provide a thin layer around the Salesforce SOAP messaging that consumes both the Enterprise and Partner WSDL formats and implements the Salesforce API 17.0 spec.',
    author = 'dlanstein',
    author_email = 'lanstein@yahoo.com',
    url = 'https://github.com/vchan/salesforce-python-toolkit',
    packages = ['sforce'],
    scripts = [],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires = [
        'suds==0.3.7',
    ],
    zip_safe = False
)
