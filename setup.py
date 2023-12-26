# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='herdy game',
      version='0.0.1',
      description='game',
      executables=executables)