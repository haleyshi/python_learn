

dict1 = {}
dict2 = {}

dict1['name'] = 'name1'
dict2['name'] = 'name2'
dict1['age'] = 10
dict2['age'] = '20'
dict1['a1'] = 'a1'
dict2['a2'] = 'a2'

dict1['list'] = []
dict1['list'].append({'name':'dict1_list_name1', 'x':'x1', 'y':'y1'})
dict1['list'].append({'name':'dict1_list_name2', 'x':'x2', 'y':'y2'})

dict2['list'] = []
dict2['list'].append({'name':'dict2_list_name1', 'a':'a1', 'b':'b1'})
dict2['list'].append({'name':'dict2_list_name2', 'a':'a2', 'b':'b2'})

print dict1
print
print dict2
dict1.update(dict2)
print
print dict1