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
