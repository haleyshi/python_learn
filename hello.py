# hello world
print "Hello Python!"

print "_".join(("a","b","c"))

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


# default argument values
def ask_ok(prompt, retries=4, complaint="Yes[y, Y, yes, YES] or No[n, N, no, NO], please!"):
	while True:
		ok = raw_input(prompt)
		if ok in ("y", "yes", "Y", "YES"):
			return True
		elif ok in ("n", "N", "no", "NO"):
			return False
		
		retries = retries -1
		if retries < 0:
			raise IOError("refusenik user")
		
		print complaint

ask_ok('Are you really want to give all your money to me?')
ask_ok("Do you want to eat a piece of pie?", 2)
ask_ok("Do you like me?", 3, "come on, use the right format for your answer!")

# pass
print "Busy wait for Ctrl+C..."
while True:
	pass

print "Orphan"

