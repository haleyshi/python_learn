# -*- coding: UTF-8 -*-

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('List Price:\w+ \$([\d.]+)')
AMZN = 'http://www.isbnsearch.org/isbn/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getPrice(isbn):
    page = uopen("%s%s" % (AMZN, isbn))
    data = page.read()
    page.close()

    return REGEX.findall(data)[0]

def showPrice(isbn):
    print '- %r with price %s' % (ISBNs[isbn], getPrice(isbn))

def main():
    print 'At', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        showPrice(isbn)

if __name__ == '__main__':
    main()