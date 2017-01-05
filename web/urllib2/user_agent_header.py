# -*- coding: utf-8 -*-

'''
伪装成浏览器，修改User-Agent
'''

import urllib2
import urllib

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

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

