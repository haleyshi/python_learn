import urllib2

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print "301"
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        print "302"
        pass

opener = urllib2.build_opener(RedirectHandler)
try:
    response = opener.open('http://rrurl.cn/b1UZuP')
except urllib2.HTTPError, e:
    print e.reason
else:
    print response.read()