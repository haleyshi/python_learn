# -*- conding: UTF-8 -*-

from random import randint
from time import ctime, sleep
from Queue import Queue
from threading import Thread, currentThread
from atexit import register

def writeQ(queue, i):
    print '[%s] [%s] producing object-[%d] for Q...' % (ctime(), currentThread().name, i)
    queue.put('object-%d' % i, block=True)
    print 'current size:', queue.qsize()

def readQ(queue):
    val = queue.get(block=True)
    print '[%s] [%s] consumed [%s] from Q...' % (ctime(), currentThread().name, val)
    print 'current size:', queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue, i)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    print '[%s] Start' % ctime()

    for i in nfuncs:
        Thread(target=funcs[i], args=(q, nloops), name=funcs[i].__name__).start()

@register
def _atexit():
    print '[%s] all DONE' % ctime()

if __name__ == '__main__':
    main()