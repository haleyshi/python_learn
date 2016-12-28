import urllib2

url1 = 'http://www.sina.com.cn'
response = urllib2.urlopen(url1)

redirected1 = response.geturl() != url1

print redirected1

url2 = 'http://rrurl.cn/b1UZuP'
response = urllib2.urlopen(url2)

redirected2 = response.geturl() != url2

print redirected2