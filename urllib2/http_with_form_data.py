import urllib2
import urllib

url = 'https://en.wikipedia.org/w/index.php?title=Special:UserLogin&action=submitlogin&type=login&returnto=Main+Page'

values = {
    'wpName1' : 'abc123@gmail.com',
    'wpPassword1' : 'abc123',
    'wpRemember' : '1'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)

response = urllib2.urlopen(req)

page = response.read()

print page

