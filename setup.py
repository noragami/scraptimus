#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
try:
    from itertools import imap, ifilter
except ImportError:
    imap = map
    ifilter = filter
from os import path
from ast import parse

if __name__ == '__main__':
    package_name = 'scraptimus'

    def get_vals(var0, var1): return imap(lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
                                          ifilter(lambda line: line.startswith(var0) or line.startswith(var1), f))

    with open('scraptimus.py') as f:
        __author__, __version__ = get_vals('__version__', '__author__')

    with open('requirements.txt') as requirements_file:
        requirements = requirements_file.read().splitlines()

    setup(name=package_name,
          author=__author__,
          version=__version__,
          description='Scrape and export the list of games found at Co-optimus website.',
          url='https://github.com/noragami/scraptimus',
          license='MIT',
          packages=[],
          keywords=['scraptimus', 'scraper', 'coop', 'games', 'co-optimus'],
          classifiers=[],
          install_requires=requirements,
          py_modules=['scraptimus'],
          zip_safe=False)
