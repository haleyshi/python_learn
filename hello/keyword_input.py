def parrot(voltage, state='a stiff', action='voom', type='Dark Killer 3.0'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(1000)
parrot(voltage=1000)
parrot(voltage=10000, action="VOOOOM")
parrot(state="a jump", voltage=20)

# *, **
def applestore(type, *arguments, **keywords):
    print "Do you have any", type, "?"
    print "Sorry, we are run out of", type, "."
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for key in keys:
        print key, ":", keywords[key]


applestore("iPad Pro", "It's very runny, sir!", "It's very very runny, sir!",
           ShopperKeeper="Steve Jobs", Client="Bill Gates", Sketch="Apple Store",
           DateTime="20151115 21:46 JPT")


# Unpacking argument list
a = [3, 6]
range(*a)

dict = {"voltage" : "1000", "state" : "breeding", "action" : "voom"}
parrot(**dict)