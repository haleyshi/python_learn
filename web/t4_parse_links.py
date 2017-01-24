from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLs = (
    'http://www.baidu.com',
    'http://www.python.org',
)

def output(x):
    print '\n'.join(sorted(set(x)))

def simpleBS(url, f):
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))  # <a href='...'></a>

def fasterBS(url, f):
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parseOnlyThese=SoupStrainer('a')))

def htmlparser(url, f):
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return

            if not hasattr(self, 'data'):
                self.data = []

            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])

    parser = AnchorParser()
    parser.feed(f.read())
    if hasattr(parser, 'data'):
        output(urljoin(url, x) for x in parser.data)

# AttributeError: 'module' object has no attribute 'simpletree'
def html5libparser(url, f):
    print 'TODO'
    #output(urljoin(url, x.attributes['href']) for x in parse(f) if isinstance(x, treebuilders.simpletree.Element) and x.name == 'a')

def process(url, data):
    print '\n*** Simple BeautifulSoup'
    simpleBS(url, data)
    data.seek(0)

    print '\n*** Fast BeautifulSoup'
    fasterBS(url, data)
    data.seek(0)

    print '\n*** HTMLParser'
    htmlparser(url, data)
    data.seek(0)

    print '\n*** html5lib parse'
    html5libparser(url, data)

def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read())
        f.close()
        process(url, data)


if __name__ == '__main__':
    main()