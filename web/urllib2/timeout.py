import urllib2
#import socket

#socket.setdefaulttimeout(10)  # 10secs
#urllib2.socket.setdefaulttimeout(10)

try:
    response = urllib2.urlopen('http://github.com/haleyshi/', timeout=10)
except Exception, e:
    print e
else:
    page = response.read()
    print page

