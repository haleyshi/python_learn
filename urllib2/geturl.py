from urllib2 import Request, urlopen

old_url = 'http://rrurl.cn/b1UZuP'

request = Request(old_url)
response = urlopen(request)

print "Old URL: %s" %old_url
print "New URL: %s" %response.geturl()