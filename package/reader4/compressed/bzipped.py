import bz2
import sys

opener = bz2.BZ2File

if __name__ == '__main__':
    f = bz2.BZ2File(sys.argv[1], mode='w')
    f.write(' '.join(sys.argv[2:]))
    f.close()