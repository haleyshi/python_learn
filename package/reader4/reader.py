import os

from reader4.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
    '.py': open
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension)
        self.f = opener(filename, 'r')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
