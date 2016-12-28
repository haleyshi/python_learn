
money = 10
bottles =0
caps = 0
price = 2
price_bottles = 2
price_caps = 4
sum = 0

print sum, money, caps, bottles

if money >= price:
    buy = money / price
    print "Use $%d to buy %d beers" % (buy*price, buy)
    money = money % price
    sum += buy
    caps += buy
    bottles += buy

print "Drinked: %d, money_left: %d, bottles_left: %d, caps_left: %d" % (sum, money, bottles, caps)

while True:
    if bottles >= price_bottles:
        buy = bottles / price_bottles
        print "Use %d bottles to exchanges %d beers" % (buy*price_bottles, buy)
        bottles = bottles % price_bottles
        sum += buy
        caps += buy
        bottles += buy

        print "Drinked: %d, money_left: %d, bottles_left: %d, caps_left: %d" % (sum, money, bottles, caps)
        continue;

    if caps >= price_caps:
        buy = caps / price_caps
        print "Use %d caps to exchanges %d beers" % (buy*price_caps, buy)
        caps = caps % price_caps
        sum += buy
        caps += buy
        bottles += buy

        print "Drinked: %d, money_left: %d, bottles_left: %d, caps_left: %d" % (sum, money, bottles, caps)
        continue;

    break;

print sum