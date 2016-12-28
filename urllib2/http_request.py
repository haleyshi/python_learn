
import urllib2

req = urllib2.Request('http://github.com/haleyshi')
#req = urllib2.Request('ftp://someserver.com/')
response = urllib2.urlopen(req)

page = response.read()

lines = page.split('\n')
for line in lines:
    line = line.strip()
    if line.startswith('<span class="repo"'):
        print line