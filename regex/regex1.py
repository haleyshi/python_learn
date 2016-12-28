#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
【整理】Python中的re.search和re.findall之间的区别和联系 + re.finall中带命名的组，不带命名的组，非捕获的组，没有分组四种类型之间的区别
http://www.crifan.com/python_re_search_vs_re_findall

Version:    2012-11-16
Author:     Crifan
"""

import re;

# 提示：
# 在看此教程之前，请先确保已经对下列内容已了解：
# 【教程】详解Python正则表达式
# http://www.crifan.com/detailed_explanation_about_python_regular_express/
# 【教程】详解Python正则表达式之： (…) group 分组
# http://www.crifan.com/detailed_explanation_about_python_regular_express_about_group/
# 【教程】详解Python正则表达式之： (?P<name>…) named group 带命名的组
# http://www.crifan.com/detailed_explanation_about_python_regular_express_named_group/

searchVsFindallStr = """
pic url test 1 http://1821.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35f9d5g213.jpg
pic url test 2 http://1881.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35ee46g213.jpg
pic url test 2 http://1802.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae361ac6g213.jpg
"""

singlePicUrlP_noGroup = "http://\w+\.\w+\.\w+.+?/\w+?.jpg"; # 不带括号，即没有group的
singlePicUrlP_nonCapturingGroup = "http://(?:\w+)\.(?:\w+)\.(?:\w+).+?/(?:\w+?).jpg"; #非捕获的组 == non-capturing group
singlePicUrlP_namedGroup = "http://(?P<field1>\w+)\.(?P<field2>\w+)\.(?P<field3>\w+).+?/(?P<filename>\w+?).jpg"; #带命名的group == named group
singlePicUrlP_unnamedGroup = "http://(\w+)\.(\w+)\.(\w+).+?/(\w+?).jpg"; #不带命名的group == unnamed group

# 1. re.search
#通过search，只能获得单个的字符串
#因为search不像findall，会去搜索所有符合条件的
foundSinglePicUrl = re.search(singlePicUrlP_namedGroup, searchVsFindallStr);
#searc只会在找到第一个符合条件的之后，就停止搜索了
print "foundSinglePicUrl=",foundSinglePicUrl; #foundSinglePicUrl= <_sre.SRE_Match object at 0x01F75230>
#然后返回对应的Match对象
print "type(foundSinglePicUrl)=",type(foundSinglePicUrl); #type(foundSinglePicUrl)= <type '_sre.SRE_Match'>
if(foundSinglePicUrl):
    #对应的，如果带括号了，即带group，是可以通过group来获得对应的值的
    field1 = foundSinglePicUrl.group("field1");
    field2 = foundSinglePicUrl.group("field2");
    field3 = foundSinglePicUrl.group("field3");
    filename = foundSinglePicUrl.group("filename");

    group1 = foundSinglePicUrl.group(1);
    group2 = foundSinglePicUrl.group(2);
    group3 = foundSinglePicUrl.group(3);
    group4 = foundSinglePicUrl.group(4);

    #field1=1821, filed2=img, field3=pp, filename=u121516081_136ae35f9d5g213
    print "field1=%s, filed2=%s, field3=%s, filename=%s"%(field1, field2, field3, filename);

    #此处也可以看到，即使group是命名了，但是也还是对应着索引号1,2,3,4的group的值的
    #两者是等价的，只是通过名字去获得对应的组的值，相对更加具有可读性，且不会出现搞混淆组的编号的问题
    #group1=1821, group2=img, group3=pp, group4=u121516081_136ae35f9d5g213
    print "group1=%s, group2=%s, group3=%s, group4=%s"%(group1, group2, group3, group4);

# 2. re.findall - no group
#通过findall，想要获得整个字符串的话，就要使用不带括号的，即没有分组
foundAllPicUrl = re.findall(singlePicUrlP_noGroup, searchVsFindallStr);
#findall会找到所有的匹配的字符串
print "foundAllPicUrl=",foundAllPicUrl; #foundAllPicUrl= ['http://1821.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35f9d5g213.jpg', 'http://1881.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35ee46g213.jpg', 'http://1802.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae361ac6g213.jpg']
#然后作为一个列表返回
print "type(foundAllPicUrl)=",type(foundAllPicUrl); #type(foundAllPicUrl)= <type 'list'>
if(foundAllPicUrl):
    for eachPicUrl in foundAllPicUrl:
        print "eachPicUrl=",eachPicUrl; # eachPicUrl= http://1821.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35f9d5g213.jpg

        #此处，一般常见做法就是，针对每一个匹配到的，完整的字符串
        #再去使用re.search处理，提取我们所需要的值
        foundEachPicUrl = re.search(singlePicUrlP_namedGroup, eachPicUrl);
        print "type(foundEachPicUrl)=",type(foundEachPicUrl); #type(foundEachPicUrl)= <type '_sre.SRE_Match'>
        print "foundEachPicUrl=",foundEachPicUrl; #foundEachPicUrl= <_sre.SRE_Match object at 0x025D45F8>
        if(foundEachPicUrl):
            field1 = foundEachPicUrl.group("field1");
            field2 = foundEachPicUrl.group("field2");
            field3 = foundEachPicUrl.group("field3");
            filename = foundEachPicUrl.group("filename");

            #field1=1821, filed2=img, field3=pp, filename=u121516081_136ae35f9d5g213
            print "field1=%s, filed2=%s, field3=%s, filename=%s"%(field1, field2, field3, filename);

# 3. re.findall - non-capturing group
#其实，此处通过非捕获的组，去使用findall的效果，其实和上面使用的，没有分组的效果，是类似的：
foundAllPicUrlNonCapturing = re.findall(singlePicUrlP_nonCapturingGroup, searchVsFindallStr);
#findall同样会找到所有的匹配的整个的字符串
print "foundAllPicUrlNonCapturing=",foundAllPicUrlNonCapturing; #foundAllPicUrlNonCapturing= ['http://1821.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35f9d5g213.jpg', 'http://1881.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35ee46g213.jpg', 'http://1802.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae361ac6g213.jpg']
#同样作为一个列表返回
print "type(foundAllPicUrlNonCapturing)=",type(foundAllPicUrlNonCapturing); #type(foundAllPicUrlNonCapturing)= <type 'list'>
if(foundAllPicUrlNonCapturing):
    for eachPicUrlNonCapturing in foundAllPicUrlNonCapturing:
        print "eachPicUrlNonCapturing=",eachPicUrlNonCapturing; #eachPicUrlNonCapturing= http://1821.img.pp.sohu.com.cn/images/blog/2012/3/7/23/28/u121516081_136ae35f9d5g213.jpg

        #此处，可以根据需要，和上面没有分组的例子中类似，再去分别处理每一个字符串，提取你所需要的值

# 4. re.findall - named group
#接着再来演示一下，如果findall中，使用了带命名的group（named group）的结果：
foundAllPicGroups = re.findall(singlePicUrlP_namedGroup, searchVsFindallStr);
#则也是可以去查找所有的匹配到的字符串的
#然后返回的是列表的值
print "type(foundAllPicGroups)=",type(foundAllPicGroups); #type(foundAllPicGroups)= <type 'list'>
#只不过，列表中每个值，都是对应的，各个group的值了
print "foundAllPicGroups=",foundAllPicGroups; #foundAllPicGroups= [('1821', 'img', 'pp', 'u121516081_136ae35f9d5g213'), ('1881', 'img', 'pp', 'u121516081_136ae35ee46g213'), ('1802', 'img', 'pp', 'u121516081_136ae361ac6g213')]
if(foundAllPicGroups):
    for eachPicGroups in foundAllPicGroups:
        #此处，不过由于又是给group命名了，所以，就对应着
        #(?P<field1>\w+) (?P<field2>\w+) (?P<field3>\w+) (?P<filename>\w+?) 这几个部分的值了
        print "eachPicGroups=",eachPicGroups; #eachPicGroups= ('1821', 'img', 'pp', 'u121516081_136ae35f9d5g213')
        #由于此处有多个group，此处类型是tuple，其中由上述四个group所组成
        print "type(eachPicGroups)=",type(eachPicGroups); #type(eachPicGroups)= <type 'tuple'>

        #此处，可以根据需要，和上面没有分组的例子中类似，再去分别处理每一个字符串，提取你所需要的值

# 5. re.findall - unnamed group
#此处再来演示一下，findall中，如果使用带group，但是是没有命名的group（unnamed group）的效果：
foundAllPicGroupsUnnamed = re.findall(singlePicUrlP_unnamedGroup, searchVsFindallStr);
#此处，肯定也是返回对应的列表类型
print "type(foundAllPicGroupsUnnamed)=",type(foundAllPicGroupsUnnamed); #type(foundAllPicGroupsUnnamed)= <type 'list'>
#而列表中每个值，其实也是对应各个组的值的组合
print "foundAllPicGroupsUnnamed=",foundAllPicGroupsUnnamed; #foundAllPicGroupsUnnamed= [('1821', 'img', 'pp', 'u121516081_136ae35f9d5g213'), ('1881', 'img', 'pp', 'u121516081_136ae35ee46g213'), ('1802', 'img', 'pp', 'u121516081_136ae361ac6g213')]
if(foundAllPicGroupsUnnamed):
    for eachPicGroupsUnnamed in foundAllPicGroupsUnnamed:
        #可以看到，同样的，每个都是一个tuple变量
        print "type(eachPicGroupsUnnamed)=",type(eachPicGroupsUnnamed); #type(eachPicGroupsUnnamed)= <type 'tuple'>
        #每个tuple中的值，仍是各个未命名的组的值的组合
        print "eachPicGroupsUnnamed=",eachPicGroupsUnnamed; #eachPicGroupsUnnamed= ('1821', 'img', 'pp', 'u121516081_136ae35f9d5g213')

        #此处，可以根据需要，和上面没有分组的例子中类似，再去分别处理每一个字符串，提取你所需要的值