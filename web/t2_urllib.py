# -*- coding: UTF-8 -*-

import urllib

# 转化成URL数据
name = 'python class'
number = 20
base = 'http://stackoverflow.com/search'
final1 = '%s?name=%s&num=%d' % (base, urllib.quote(name), number)
final2 = '%s?name=%s&num=%d' % (base, urllib.quote_plus(name), number)

print urllib.unquote(urllib.quote(name))
print urllib.unquote_plus(urllib.quote_plus(name))
print final1
print final2
print

# 转化字典为URL数据
dict = {'name': "Georgy Clooney", 'age': 47, 'abc': '~hello'}
print urllib.urlencode(dict)
print

# 打开Web连接，返回文件对象
f = urllib.urlopen('http://weather.sina.com.cn/guangzhou')
print '################# f.info() ############'
print f.info()
print
print '################# f.readline() ############'
print f.readline()
print
print '################# f.read(1024) ############'
print f.read(1024)  ## 1024 Bytes from current cursor
print
print '################# f.geturl() ############'
print f.geturl()  ## Return the real URL
#all_lines_list = f.readlines()
#all_content_string = f.read()
f.close()


# Save to file
urllib.urlretrieve('http://quote.yahoo.com/d/quotes.csv?s=ERIC,ERIC-A.ST,ERIC-B.ST&f=sl1clp2', filename='eric.csv')