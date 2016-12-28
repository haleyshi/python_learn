#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
【教程】详解Python正则表达式之： (?P<name>...) named group 带命名的组
http://www.crifan.com/detailed_explanation_about_python_named_group

Version:    2012-11-12
Author:     Crifan
"""

import re;

#如下教程所举例的代码，已去除重复的，关于group本身的解释。
#所以，请在参考学习下面代码之前，请确保已经对group的用法有所了解。
#如不了解，可参考：
#【教程】详解Python正则表达式之： (…) group 分组
#http://www.crifan.com/detailed_explanation_about_python_regular_express_about_group/

# 下列举例所用的字符串是来自于 http://janexyy.blogbus.com/logs/105359907.html 中的部分html代码
# 此处所采用的示例代码，参考自：
#http://code.google.com/p/blogs-to-wordpress/source/browse/trunk/libs/crifan/blogModules/BlogBlogbus.py
# -> extractTags()
reNamedGroupTestStr = u'标签：<a href="/tag/情侣电话粥/">情侣电话粥</a>';

# 1. (?P=name)
# 此处就是通过 (?P=name)的方式，来引用，正则表达式中，前面已经命名tagName的group的
foundTagA = re.search(u'.+?<a href="/tag/(?P<tagName>.+?)/">(?P=tagName)</a>', reNamedGroupTestStr);
print "foundTagA=",foundTagA; #foundTagA= <_sre.SRE_Match object at 0x00876D60>

if(foundTagA):
    # 2. mateched.group(name)
    # 可以通过之前给group命的名，来获得匹配到的值
    namedGroupStr = foundTagA.group("tagName");
    print "namedGroupStr=",namedGroupStr; #namedGroupStr= 情侣电话粥

    # 3. matched.group(N) == matched.group(name)
    # 此处，通过group的index，即group(1),group(2),...
    # 也可以获得和之前通过名字name获得的group的值
    # 通过名字或者索引号，两种方式都可以获得所需要的值，
    # 但是通过名字，更加准确，不会出现，当group太多而index容易混淆的问题
    group1Value = foundTagA.group(1);
    print "Group(1): group1Value=",group1Value; #Group(1): group1Value= 情侣电话粥

    # 4. \g<name> in re.sub()
    # 在re.sub()中，通过\g<name>的方式，引用前面已经命名为name的group的值
    substitutedStr = re.sub(u'.+?<a href="/tag/(?P<tagName>.+?)/">(?P=tagName)</a>', u'所捕获的tag值为：\g<tagName>', reNamedGroupTestStr);
    print "Original string=%s, after substituted=%s"%(reNamedGroupTestStr, substitutedStr); #Original string=标签：<a href="/tag/情侣电话粥/">情侣电话粥</a>, after substituted=所捕获的tag值为：情侣电话粥
