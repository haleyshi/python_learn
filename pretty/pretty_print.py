import json
import pprint
from urllib2 import Request, urlopen

request = Request('http://pypi.python.org/pypi/configparser/json')
response = urlopen(request)
http_info = response.info()

raw_data = response.read().decode("utf-8")

project_info = json.loads(raw_data)
result = {'headers': http_info.items(), 'body': project_info}

pprint.pprint(result)