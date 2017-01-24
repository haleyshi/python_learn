'''
阴阳师里面，N卡是二星的（几乎所有的卡初始都是二星的）。

一个2星的狗粮（一般是N卡）升满了20级就可以吃两个1级的N卡变成20级的3星；
3星的升满到25级吃3个20级的3星卡就可以变成25级的4星；
4星的升满到30级吃4个25级的4星卡就可以升成30级的5星；
5星的升满到35级就可以吃5个30级的5星卡变成6星。

So，
假设我有一张升满到35级的SSR卡，还需要吃多少个N卡才能升到6星？
每张N卡需要升那些等级的阶段（1-20， 20-25， 25-30）？

请用小于20行代码求解。
'''


dog_food_n20 = {"n1": 1, "1_to_20": 1}
dog_food_star3 = {"dog_food_n20": 1, "n1": 2}
dog_food_n25 = {"dog_food_star3": 1, "20_to_25": 1}
dog_food_star4 = {"dog_food_n25": 1, "dog_food_star3": 3}
dog_food_n30 = {"dog_food_star4": 1, "25_to_30": 1}
dog_food_star5 = {"dog_food_n30": 1, "dog_food_star4": 4}

ssr4 = {"dog_food_star3": 3}
ssr5 = {"dog_food_star4": 4}
ssr6 = {"dog_food_star5": 5}

def convert(material=ssr4):
    for req in material.keys():
        if req.startswith('dog_food'):
            for num in range(0, material[req]):
                convert(eval(req))
        else:
            if reqs.has_key(req):
                reqs[req] = reqs[req] + material[req]
            else:
                reqs[req] = material[req]

reqs = {}
convert(ssr6)
print reqs

reqs = {}
convert(ssr5)
print reqs

reqs = {}
convert(ssr4)
print reqs