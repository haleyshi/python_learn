
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