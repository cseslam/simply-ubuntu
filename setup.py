#!/usr/bin/python

from DistUtilsExtra.auto import setup

APP_NAME = "Simply Ubuntu"
VERSION = '1.0'
AUTHOR = "Eslam Mostafa"
AUTHOR_EMAIL = 'me@eslammostafa.com'
LICENSE = "GPL"
DESC = 'A simple app that fixes arabic probelms in ubuntu'

setup(name=APP_NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      description=DESC,
      packages=['simply-ubuntu'],
      scripts=['bin/simply-ubuntu',],
      data_files=[],
)
