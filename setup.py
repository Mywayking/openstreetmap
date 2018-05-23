# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/23
-------------------------------------------------
   Description:
-------------------------------------------------
"""

from setuptools import setup,find_packages
from openstreemap import __version__

VERSION = __version__

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
    url='https://git.rtbasia.com/galen/openstreetmap',
    keywords='openstreetmap',
    packages=find_packages(),
    install_requires=[
        'lxml',
        'requests',
    ],
)
