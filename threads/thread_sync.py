import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print "Starting", self.name
        threadLock.acquire()
        print_time(self.name, self.counter, self.delay)
        threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s : %d : %s" % (threadName, counter, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "Thread-A", 8, 3)
thread2 = myThread(2, "Thread-B", 5, 4)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print "Exit Main Thread!"

