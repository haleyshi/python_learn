from distutils.core import setup, Extension

MOD = 'Test1'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['t1_ext.c'])])