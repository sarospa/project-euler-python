import time

primes = [2]

def generate_primes(n):
	p = primes[len(primes) - 1]
	count = 0
	while count < n:
		is_prime = True
		for i in range(0, len(primes)):
			if p % primes[i] == 0:
				is_prime = False
				break
		if is_prime:
			count = count + 1
			primes.append(p)
		p = p + 1

def is_palindrome(val):
	str_val = str(val)
	for i in range(0, len(str_val) // 2):
		if str_val[i] != str_val[-(i + 1)]:
			return False
	return True

def print_runtime(func):
	start_time = time.perf_counter()
	func()
	runtime = time.perf_counter() - start_time
	print("Solved in %.3f seconds." % runtime)