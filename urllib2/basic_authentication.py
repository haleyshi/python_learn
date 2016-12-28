import urllib2

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()

top_level_url = "http://www.sina.com.cn"

password_manager.add_password(None, top_level_url, 'user123', 'password123')

handler = urllib2.HTTPBasicAuthHandler(password_manager)

opener = urllib2.build_opener(handler)

url = 'http://news.sina.com.cn/c/nd/2016-01-15/doc-ifxnrahr8333154.shtml'

response = opener.open(url)

page = response.read()

print page

#urllib2.install_opener(opener)