#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

from distutils.core import setup
import py2exe

setup(
    name="Simple_Rat",
    version="1.0",
    description="Malware de conexion inversa",
    author="Larm182(Aureliohacking)",
    author_email="aureliohacking182@gmail.com",
    url="https://github.com/larm182",
    license="Licencia 1.0",
    scripts=["client.py"],
    console=["client.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)