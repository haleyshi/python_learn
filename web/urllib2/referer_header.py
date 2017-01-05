# -*- coding: utf-8 -*-

'''
对付反盗链，修改请求header中的Referer为网站自身
'''

import urllib2
import urllib

header = {'Referer':'http://www.taobao.com'}

values = {
    'wpName1' : 'abc123',
    'wpPassword1' : 'abc123',
    'wpRemember' : '1'
}

postdata = urllib.urlencode(values)

req = urllib2.Request(url='http://www.taobao.com', data=postdata, headers=header)

response = urllib2.urlopen(req)

page = response.read()

print page

