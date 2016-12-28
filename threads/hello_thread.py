# -*- coding: UTF-8 -*-

import thread
import time

def printTime(threadName, delay, repeats):
    count = 0
    while count < repeats:
        count += 1
        time.sleep(delay)
        print "%s : %d : %s" % (threadName, count, time.ctime(time.time()))

# 创建线程
try:
    thread.start_new_thread(printTime, ("Thread-A", 5, 8, ))
    thread.start_new_thread(printTime, ("Thread-B", 7, 5, ))
except:
    print "Unable to start new thread."

while 1:
    pass
