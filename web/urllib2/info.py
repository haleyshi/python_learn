from urllib2 import Request, urlopen

url = 'http://www.baidu.com'

req = Request(url)
response = urlopen(req)

headers = response.info()

#if headers.has_key("Server"):
#    print headers["Server"]

print headers