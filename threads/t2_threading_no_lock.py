# -*- coding: utf-8 -*-

from threading import Thread, currentThread
from time import sleep, ctime
from atexit import register
from random import randrange

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2,5) for x in xrange(randrange(3,7)))

remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    remaining.add(myname)
    print '[%s] Started %s' % (ctime(), myname)
    sleep(nsec)
    remaining.remove(myname)
    print '[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)
    print '     (remaining: %s)' % (remaining or 'NONE')

def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

if __name__ == '__main__':
    main()