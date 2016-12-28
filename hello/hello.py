# hello world
print "Hello Python!"

# if, method
def howMany(x):
	if x < 0:
		x = 0
		print "Negative changed to zero"
	elif x == 0:
		print "Zero"
	elif x == 1:
		print "Single"
	else:
		print "More"

howMany(-5)
howMany(0)
howMany(1)
howMany(1000)

# for, list
words = ["Yokohama", "Tokyo", "Yokosuca"]

# range
for word in words:
	print word, len(word)

lyrics = ["Mary", "has", "a", "little", "lamb"]

for i in range(len(lyrics)):
	print i, lyrics[i]

# break
for n in range(2, 20):
	for x in range(2, n/2+1):
		if n % x == 0:
			print n, "=", x, "*", n/x
			break
	else:
		print n, "is a prime number"

# continue
for n in range(1, 10):
	if n % 2 == 0:
		print n, "is an even number"
		continue
	print n, "is an odd number"

# method, print in same line
def fib(n):
	a, b = 0, 1

	while a < n:
		print a,
		a, b = b, a+b

	print

fib(2000)

# pass
def intlog(*args):
	pass

class MyClass:
	pass

# default value calculation
x = 5

def method1(arg=x):
    print arg

x = 6
method1()

# List but not default value
def appendToList(a, L=[]):
    L.append(a)
    print L

appendToList(1)
appendToList(3)
appendToList(5)

def appendToList2(a, L=None):
    if L == None:
        L = []
    L.append(a)
    print L

appendToList2(1)
appendToList2(3)
appendToList2(5, [])
appendToList2(7, [])
appendToList2(9, [2, 4])


