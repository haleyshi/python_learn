import urllib2
import urllib

url = 'http://127.0.0.1:8080/v1/user/'
values = {
    'name' : 'abc123',
    'age' : '20',
    'sex' : 'male'
}
data = urllib.urlencode(values)

request = urllib2.Request(url, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)

print response.read()