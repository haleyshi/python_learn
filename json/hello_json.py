import demjson

data = [{"name" : "Shi Qiyang", "age" : 4, "sex" : "male", "nickname" : "baozi"}]

json = demjson.encode(data)

print json

text = demjson.decode(json)

print text