# -*- coding: utf-8 -*-

from atexit import register
from threading import Thread
from time import ctime
from urllib2 import urlopen, Request, HTTPError
import json

site = 'https://api.douban.com/v2/book/'
books = {
    '1220562': 'White Whale',
    '1220563': 'Baby',
    '1220588': 'Movie',
    '1220888': 'matlab',
}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

def getRanking(book):
    req = Request("%s%s" % (site, book), headers=hdr)

    try:
        page = urlopen(req)
    except HTTPError, e:
        print e.fp.read()

    data = page.read()
    page.close()

    return json.loads(data)['rating']['average']

def showRanking(book):
    print '- %r with ranking %s' % (books[book], getRanking(book))

def main():
    print 'At', ctime(), 'on Douban:'
    for book in books:
        Thread(target=showRanking, args=(book,)).start()
        #showRanking(book)

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()