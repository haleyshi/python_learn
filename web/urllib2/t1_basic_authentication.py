import urllib2

LOGIN='your_username'
PASSWD = 'your_password'
URL = 'https://github.com/haleyshi/python_learn'
REALM = 'Secure Archive'

def handler_version(url):
    from urlparse import urlparse
    handler = urllib2.HTTPBasicAuthHandler()
    handler.add_password(REALM, urlparse(url).netloc, LOGIN, PASSWD)  # Use the top level URL
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    request = urllib2.Request(url)
    base64string = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]  ## Remove the last CRLF
    request.add_header('Authentication', 'Basic %s' % base64string)
    return request

for funcType in ('handler', 'request'):
    print '*** Using %s:' %funcType.upper()
    url = eval('%s_version' % funcType)(URL)
    f = urllib2.urlopen(url)
    print f.info()
    print
    f.close()