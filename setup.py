#!/usr/bin/env python

import os
import setuptools

def get_long_description():
    filename = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(filename) as f:
        return f.read()

setuptools.setup(name='oncore',
      version='0.0.1',
      description="Oncore: utilities from OffNote Labs",
      long_description=get_long_description(),
      long_description_content_type="text/markdown",
      author='Nishant Sinha',
      author_email='nishant@offnote.co',
      url='https://github.com/ofnote/oncore',
      license='Apache 2.0',
      platforms=['POSIX'],
      packages=setuptools.find_packages(),
      #entry_points={},
      #scripts=['scripts/tsa'],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
          ],

      setup_requires=[],
      install_requires=[],
      )