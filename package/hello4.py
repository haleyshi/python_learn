import reader4

r = reader4.Reader('test.gz')
print r.read()
r.close()

r = reader4.Reader('test.bz2')
print r.read()
r.close()

r = reader4.Reader('reader4/__init__.py')
print r.read()
r.close()