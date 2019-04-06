import time

primes = []

# n is the number of primes to generate.
def generate_primes(n):
	if len(primes) == 0:
		p = 2
	else:
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

# generates all primes between 1 and n.
def generate_primes_sieve(n):
	prime_sieve = [True] * n
	prime_sieve[0] = False
	prime_sieve[1] = False
	for i in range(1, n):
		if prime_sieve[i]:
			primes.append(i)
			for j in range(i, n, i):
				prime_sieve[j] = False

def triangle(n):
	return (n * (n + 1)) // 2
				
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