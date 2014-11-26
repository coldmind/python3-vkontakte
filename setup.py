#!/usr/bin/env python
from distutils.core import setup

version='1.0.0'

setup(
    name='vkontakte',
    version=version,
    author='Andriy Sokolovskiy',
    author_email='',
    requires=['requests', ],
    packages=['vkontakte'],

    url='https://github.com/coldmind/python3-vkontakte',
    license = 'MIT license',
    description = "vk.com (aka vkontakte.ru) API wrapper",

    long_description = open('README.rst').read() + open('CHANGES.rst').read(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
