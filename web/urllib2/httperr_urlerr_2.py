from urllib2 import Request, urlopen, URLError

req = Request('http://blog.csdn.net/sgh')

try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'code'):
        print e.code

    elif hasattr(e, 'reason'):
        print e.reason

else:
    print "Success"