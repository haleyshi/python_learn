import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print "Starting", self.name
        print_time(self.name, self.counter, self.delay)
        print "Exiting", self.name

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threading.exit()

        time.sleep(delay)
        print "%s : %d : %s" % (threadName, counter, time.ctime(time.time()))
        counter -= 1

thread1 = myThread(1, "Thread-A", 8, 5)
thread2 = myThread(2, "Thread-B", 5, 7)

thread1.start()
thread2.start()

print "Exiting main thread."
