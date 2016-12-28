# -*- coding=UTF-8 -*-

import re

sep = '-----'

print "模式匹配字符串"
m = re.match('foo', 'foo')
print '1.1', 'foo', sep, 'foo'
if m is not None:
    print m.group()

m = re.match('foo', 'bar')
print '1.2', 'foo', sep, 'bar'
if m is not None:
    print m.group()

#从起始部分匹配
m = re.match('foo', 'food supply')
print '1.3', 'foo', sep, 'food supply'
if m is not None:
    print m.group()

print '1.4', 'foo', sep, 'enough food supply'
m = re.match('foo', 'enough food supply')
if m is not None:
    print m.group()


print
print "搜索字符串"
m = re.search('foo', 'enough food supply')
print '2.1', 'foo', sep, 'enough food supply'
if m is not None:
    print m.group()


print
print '匹配多个字符串'
bt = 'bat|bet|bit'

print '3.1', bt, sep, 'bat'
m = re.match(bt, 'bat')
if m is not None:
    print m.group()

print '3.2', bt, sep, 'blt'
m = re.match(bt, 'blt')
if m is not None:
    print m.group()

print '3.3', bt, sep, 'he bit me!'
m = re.search(bt, 'he bit me!')
if m is not None:
    print m.group()


print
print '匹配单个字符'
anyend = '.end'

print '4.1', anyend, sep, 'bend'
m = re.match(anyend, 'bend')
if m is not None:
    print m.group()

print '4.2', anyend, sep, 'end'
m = re.match(anyend, 'end')
if m is not None:
    print m.group()

print '4.3', anyend, sep, 'weekend'
m = re.match(anyend, 'weekend')
if m is not None:
    print m.group()

print '4.4', anyend, sep, '\\nend'
m = re.match(anyend, '\nend')   #不匹配\n
if m is not None:
    print m.group()

print '4.5', anyend, sep, 'The end.'
m = re.search(anyend, 'The end.')
if m is not None:
    print m.group()

patt314 = '3.14'
pi_patt = '3\.14'  #转义

print '4.6', pi_patt, sep, '3.14'
m = re.match(pi_patt, '3.14')
if m is not None:
    print m.group()

print '4.7', patt314, sep, '3.14'
m = re.match(patt314, '3.14')
if m is not None:
    print m.group()

print '4.8', patt314, sep, '3014'
m = re.match(patt314, '3014')
if m is not None:
    print m.group()


print
print '创建字符集'

pt1 = '[cr][23][dp][o2]'
pt2 = 'r2d2|c3po'

print '5.1', pt1, sep, 'c3po'
m = re.match(pt1, 'c3po')
if m is not None:
    print m.group()

print '5.2', pt1, sep, 'c2do'
m = re.match(pt1, 'c2do')
if m is not None:
    print m.group()

print '5.3', pt2, sep, 'r2d2'
m = re.match(pt2, 'r2d2')
if m is not None:
    print m.group()

print '5.4', pt2, sep, 'c2do'
m = re.match(pt2, 'c2do')
if m is not None:
    print m.group()


print
print '重复，特殊字符及分组'

patt = '\w+@(\w+\.)?\w+\.com'

print '6.1', patt, sep, 'nobody@xxx.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print m.group()

print '6.2', patt, sep, 'nobody@xxx.yyy.com'
m = re.match(patt, 'nobody@xxx.yyy.com')
if m is not None:
    print m.group()

print '6.3', patt, sep, 'nobody@xxx.yyy.zzz.com'
m = re.match(patt, 'nobody@xxx.yyy.zzz.com')
if m is not None:
    print m.group()

patt = '\w+@(\w+\.)*\w+\.com'
print '6.4', patt, sep, 'nobody@xxx.yyy.zzz.com'
m = re.match(patt, 'nobody@xxx.yyy.zzz.com')
if m is not None:
    print m.group()

patt = '\w\w\w-\d\d\d'
print '6.5', patt, sep, 'abc-123'
m = re.match(patt, 'abc-123')
if m is not None:
    print m.group()

print '6.6', patt, sep, 'abc-xyz'
m = re.match(patt, 'abc-xyz')
if m is not None:
    print m.group()

patt = '(\w\w\w)-(\d\d\d)'
print '6.7', patt, sep, 'abc-123'
m = re.match(patt, 'abc-123') #子组
if m is not None:
    print m.group()
    print m.group(1)
    print m.group(2)
    print m.groups()

patt = 'ab'
print '6.8', patt, sep, 'ab'
m = re.match(patt, 'ab')
if m is not None:
    print m.group()
    print m.groups()

patt = '(ab)'
print '6.9', patt, sep, 'ab'
m = re.match(patt, 'ab')
if m is not None:
    print m.group()
    print m.group(1)
    print m.groups()

patt = '(a)(b)'
print '6.10', patt, sep, 'ab'
m = re.match(patt, 'ab')
if m is not None:
    print m.group()
    print m.group(1)
    print m.group(2)
    print m.groups()

patt = '(a(b))'
print '6.11', patt, sep, 'ab'
m = re.match(patt, 'ab')
if m is not None:
    print m.group()
    print m.group(1)
    print m.group(2)
    print m.groups()


print
print '起始，结尾及单词边界'

patt = '^The' # 起始

print '7.1', patt, sep, 'The end.'
m = re.search(patt, 'The end.')
if m is not None:
    print m.group()

print '7.2', patt, sep, 'Show Me The Money.'
m = re.search(patt, 'Show Me The Money.')
if m is not None:
    print m.group()

patt = r'\bthe'  # 边界

print '7.3', patt, sep, 'Show me the money.'
m = re.search(patt, 'Show me the money.')
if m is not None:
    print m.group()

print '7.4', patt, sep, 'Show methe money.'
m = re.search(patt, 'Show methe money.')
if m is not None:
    print m.group()

patt = r'\Bthe'  # 无边界
print '7.5', patt, sep, 'Show methe money.'
m = re.search(patt, 'Show methe money.')
if m is not None:
    print m.group()


print
print 'findall() and finditer()'

print '8.1', 'car', sep, 'car'
print re.findall('car', 'car')

print '8.2', 'car', sep, 'scary'
print re.findall('car', 'scary')

print '8.3', 'car', sep, 'carry the barcardi to the car'
print re.findall('car', 'carry the barcardi to the car')

s = 'This and that.'
patt = r'(th\w+) and (th\w+)'

print '8.4', patt, sep, s
print re.findall(patt, s, re.I)  #忽略大小写

print '8.5', patt, sep, s
print re.finditer(patt, s, re.I).next().groups()
print re.finditer(patt, s, re.I).next().group(1)
print re.finditer(patt, s, re.I).next().group(2)
print re.finditer(patt, s, re.I).next().group()

patt = r'(th\w+)'

print '8.6', patt, sep, s
print re.findall(patt, s, re.I)

print '8.7', patt, sep, s

iter = re.finditer(patt, s, re.I)

item = iter.next()
print item.groups()
print item.group(1)

item = iter.next()
print item.groups()
print item.group(1)

for item in re.finditer(patt, s, re.I):
    print item.group(1)

print [item.group(1) for item in re.finditer(patt, s, re.I)]


print
print "搜索和替换"

repsep = '>>>'

s = 'attn: X\n\nDear X,\n'
fs = 'X'
ts = 'Mr. Smith'
print '9.1', fs, repsep, ts, sep, r'attn: X\n\nDear X,\n'
print re.sub(fs, ts, s)
print re.subn(fs, ts, s)

s = 'abcdef'
fs = '[ae]'
ts = 'X'
print '9.2', fs, repsep, ts, sep, s
print re.sub(fs, ts, s)
print re.subn(fs, ts, s)

s = '2/20/16'
fs = r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})'
ts = r'\2/\1/\3'
print '9.3', fs, repsep, ts, sep, s
print re.sub(fs, ts, s)

s = '2/20/2016'
print '9.4', fs, repsep, ts, sep, s
print re.sub(fs, ts, s)


print
print '分隔字符串'

print '10.1', ':', sep, 'str1:str2:str3'
print re.split(':', 'str1:str2:str3')

DATA = (
    'Guangzhou, GD 510000',
    'Shenzhen, GD',
    'Foshan, 528000',
    'Zhuhai 519000',
    'Dongguan GD'
)
sk = ', |(?= (?:\d{6}|[A-Z]{2})) '  # ?:... 匹配一个不用保存的分组  ?=... 正向前视断言，如果...出现在出现在之后的位置
print '10.2', sk
for datam in DATA:
    print sep, datam
    print re.split(sk, datam)


print
print '扩展符号'

patt = r'(?i)yes'   # (?i) re.I/IGNORECASE 忽略大小写
s = 'yes? Yes. YES!!'
print '11.1', patt, sep, s
print re.findall(patt, s)

patt = r'(?i)th\w+'   # 忽略大小写
s = 'The quickest way is through this tunnel.'
print '11.2', patt, sep, s
print re.findall(patt, s)

patt = r'(?im)(^th[\w ]+)'   # (?m) re.M/MULTILINE 多行混合
s = """
This line is the 1st line,
another line,
that line, it's the best
"""
print '11.3', patt, sep, s
print re.findall(patt, s)

patt = r'th.+'   # . 任何字符，除\n
s = '''
The first line
the second line
the third line
'''
print '11.4', patt, sep, s
print re.findall(patt, s)

patt = r'(?s)th.+'   # (?s)  re.S/DOTALL . 能够用来表示 \n
print '11.5', patt, sep, s
print re.findall(patt, s)

# (?x) re.X/VERBOSE 抑制在正则表达式中使用空白符（反斜杠转义除外），可用#做注释，用于创建更加易读的正则表达式
patt = r'''(?x)
    \((\d{3})\)     #区号，子组1
    [ ]             #空白符
    (\d{3})         #前缀，子组2
    -               #横线
    (\d{4})         #数字，子组3
'''
s = '(800) 555-1212'

print '11.6', patt, sep, s
m = re.search(patt, s)
if m is not None:
    print m.groups()

patt = r'http://(?:\w+\.)*(\w+\.com)'   # (?:...) 定义不保存的分组
s = 'http://google.com http://www.google.com http://developer.google.com'
print '11.7', patt, sep, s
print re.findall(patt, s)

patt = r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})'  # (?P<name>...)  使用名称标识符而非增量数字来保存匹配
s = '(800) 555-1212'
print '11.8', patt, sep, s
m = re.search(patt, s)
if m is not None:
    print m.groups()
    print m.groupdict()

ts = '(\g<areacode>) \g<prefix>-xxxx'   # \g<name> 检索保存的分组
print '11.9', patt, repsep, ts, sep, s
print re.sub(patt, ts, s)

# 丑陋版
patt = r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)'
s = '(800) 555-1212 800-555-1212 18005551212'
print '11.10', patt, sep, s
print bool(re.match(patt, s))

# 易读版
patt = r'''(?x)
    # match (800) 555-1212, save areacode, prefix, number
    \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

    # space, 空格需要转义或者定义在字符类中
    [ ]

    # match 800-555-1212
    # (?P=name) 在同一个正则表达式中重用模式
    (?P=areacode)-(?P=prefix)-(?P=number)

    #space
    [ ]

    #match 18005551212
    1(?P=areacode)(?P=prefix)(?P=number)
'''
print '11.11', patt, sep, s
print bool(re.match(patt, s))

patt = r'\w+(?= van Rossum)'
s = '''
    Guido van Rossum
    Tim Peters
    Alex Martelli
    Just van Rossum
    Raymond Hettinger
'''
print '11.12', patt, sep, s
print re.findall(patt, s)

patt = r'(?m)^\s+(?!noreply|postmaster)(\w+)'  # (?!...) 负向前视断言
s = '''
    sales@compact.com
    postmaster@compact.com
    eng@compact.com
    noreply@compact.com
    admin@compact.com
'''
print '11.13', patt, sep, s
print re.findall(patt, s)

print '11.14', patt, sep, s
print ['%s@hp.com' % item.group(1) for item in re.finditer(patt, s)]

patt = r'(?:(x)|y)(?(1)y|x)'

s = 'xy'
print '11.15', patt, sep, s
print bool(re.search(patt, s))

s = 'yx'
print '11.16', patt, sep, s
print bool(re.search(patt, s))

s = 'xx'
print '11.17', patt, sep, s
print bool(re.search(patt, s))

s = 'yy'
print '11.18', patt, sep, s
print bool(re.search(patt, s))