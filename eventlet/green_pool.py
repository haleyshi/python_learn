import eventlet
from eventlet.green import urllib2

urls = [
    "http://www.baidu.com",
    "http://www.whu.edu.cn",
    "http://www.163.com",
    "http://www.sina.com.cn"
]

pool = eventlet.GreenPool()

def fetch(url):
    return url, urllib2.urlopen(url).read()

for (url, body) in pool.imap(fetch, urls):
    print "get body %d for url: %s" % (len(body), str(url))

