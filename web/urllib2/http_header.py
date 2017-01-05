import urllib
import urllib2

url = 'https://en.wikipedia.org/w/index.php?title=Special:UserLogin&action=submitlogin&type=login&returnto=Main+Page'

values = {
    'wpName1' : 'abc123',
    'wpPassword1' : 'abc123',
    'wpRemember' : '1'
}

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = {'User-Agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req)

page = response.read()

print page