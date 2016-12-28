__author__ = 'eguoshi'

'''
Standard Producer/Consumer Threading Pattern
'''

import time
import threading
import Queue

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved
            msg = self._queue.get()
            # Checks if the current message is the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exit the loop
                break
            # "Processes"
            print "I'm a thread, and I received %s!!" % msg

        # Always be friendly!
        print 'Bye bye!'


def Producer():
    # Queue is used to share items between the threads
    queue = Queue.Queue()

    # Create and instance of worker
    worker = Consumer(queue)
    # Start calls the internal run() method to kick off the thread
    worker.start()

    # variable to keep track of when we started
    start_time = time.time()
    # While under 5 seconds
    while time.time() - start_time < 5:
        # 'Produce' a piece of work and stick it in the queue for the Consumer to process
        queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)

    # This is the "Poison Pill" method to kill a thread
    queue.put('quit')
    # wait for the thread to close down
    worker.join()


if __name__ == '__main__':
    Producer()


