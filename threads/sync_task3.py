__author__ = 'eguoshi'

'''
A more flexible way
'''

import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.apple.com',
    'http://www.google.com',
    'http://www.amazon.com',
    'http://www.microsoft.com',
    'http://www.ericsson.com',
    'http://www.sony.com',
    'http://www.samsung.com',
    'http://www.htc.com'
]

# Make the Pool of workers
pool = ThreadPool(4)

# open the URLs in their own threads and return the results
results = pool.map(urllib2.urlopen, urls)

# Close the pool and wait for the work to finish
pool.close()
pool.join()