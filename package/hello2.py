import reader2.reader as rd

print rd.__file__

r = rd.Reader('reader2/reader.py')
print r.read()
r.close()