"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/23
-------------------------------------------------
   Description:
-------------------------------------------------
"""
# !/usr/bin/env python
# coding: utf8

import sys

from setuptools import setup
from openstreemap import __version__

VERSION = __version__
sys.path.pop(0)

with open('README.rst') as fp:
    README = fp.read()

setup(
    name='openstreetmap',
    version=VERSION,
    description='OpenStreetMap coordinates',
    long_description='Extracting OpenStreetMap coordinates by name or relation id.',
    license='',
    author='galen',
    author_email='galen.wang@rtbasia.com',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    url='https://github.com/xlzd/xart',
    packages=['xart', 'xart.fonts'],
    package_data={'xart.fonts': ['*.flf', '*.flc']},
    entry_points={
        'console_scripts': [
            'xart = xart:main',
        ],
    }
)
