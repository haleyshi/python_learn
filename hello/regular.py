import re

print re.match('www', 'www.google.com').span()
print re.match('com', 'www.google.com')

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print matchObj.group()
    print matchObj.group(1)
    print matchObj.group(2)
else:
    print 'No Match!'

print re.search('www', 'www.google.com').span()
print re.search('com', 'www.google.com').span()

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print searchObj.group()
    print searchObj.group(1)
    print searchObj.group(2)
else:
    print 'No Match!'

matchObj1 = re.match(r'dog', line, re.M|re.I)

if matchObj1:
    print matchObj1.group()
else:
    print 'No Match!'

searchObj1 = re.search(r'dog', line, re.M|re.I)

if searchObj1:
    print searchObj1.group()
else:
    print 'No Match!'

phone = "139-2211-7419 # This is my phone number"
num = re.sub(r'#.*$', "", phone)
print num

num = re.sub(r'\D', "", phone)
print num