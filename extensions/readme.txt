gcc $(pkg-config --cflags --libs python2) -Wall t1_ext.c -o Test1

python setup.py build
python setup.py install
python t1_test.py