import time
import math

primes = []

# Resets all state within utilities.py, for testing purposes.
def reset():
	primes.clear()

# n is the number of primes to generate.
def generate_primes(n):
	if len(primes) == 0:
		p = 2
	else:
		p = primes[len(primes) - 1]
	count = 0
	while count <= n:
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
	primes.clear()
	prime_sieve = [True] * n
	prime_sieve[0] = False
	prime_sieve[1] = False
	for i in range(1, n):
		if prime_sieve[i]:
			primes.append(i)
			for j in range(i, n, i):
				prime_sieve[j] = False

def is_prime(n):
	for p in primes:
		if n == p or p * p > n:
			return True
		elif n % p == 0:
			return False
	return True

def triangle(n):
	return (n * (n + 1)) // 2
				
def pentagon(n):
	return (n * (3 * n - 1)) // 2

def hexagon(n):
	return n * (2 * n - 1)
	
def is_palindrome(val):
	str_val = str(val)
	for i in range(0, len(str_val) // 2):
		if str_val[i] != str_val[-(i + 1)]:
			return False
	return True

def sum_divisors(n):
	divisors = set()
	for j in range(2, round(math.sqrt(n) + 1)):
		if n % j == 0:
			divisors.add(j)
			divisors.add(n // j)
	return sum(divisors) + 1

def read_to_2d_list(filename):
	list = []
	with open(filename) as f:
		for line in f.readlines():
			dataline = []
			for num in line.split():
				dataline.append(int(num))
			list.append(dataline)
	return list

def print_runtime(func):
	start_time = time.perf_counter()
	result = func()
	runtime = time.perf_counter() - start_time
	print(result)
	print("Solved in %.3f seconds." % runtime)