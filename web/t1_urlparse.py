import urlparse
import os

parse_result =urlparse.urlparse("https://www.google.com/webhp?sourceid=chrome-instant&rlz=1C1CHBD_en__693SE695&ion=1&espv=2&ie=UTF-8#q=python")
print parse_result
print parse_result[1]  ## parse_result.netloc
print 'schema -', parse_result.scheme
print 'netloc -', parse_result.netloc
print 'path -', parse_result.path
print 'params -', parse_result.params
query = parse_result.query
print 'query -', query

q_list = query.split('&')
q_dict = {}
for q in q_list:
    kv = q.split('=')
    if len(kv) == 2:
        q_dict[kv[0]] = kv[1]

print q_dict

print 'fragment -', parse_result.fragment

print
print os.path.splitext(urlparse.urlparse('http://user@www.test.com:8090/test1/test2/test3.htm').path)

print
print urlparse.urljoin('http://www.test0.com/test1/test2/11233.html', 'test3/test4/test5.html')