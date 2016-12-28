import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting", self.name
        process_data(self.name)
        print "Exiting", self.name

def process_data(name):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = workQueue.get()
            queueLock.release()
            print "%s process %s" % (name, data)
        else:
            queueLock.release()

        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]

queueLock = threading.Lock()
workQueue = Queue.Queue(10)

threads = []
threadID = 1

for tName in threadList:
    thread = myThread(threadID,tName)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for name in nameList:
    workQueue.put(name)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print "Exiting main thread!"