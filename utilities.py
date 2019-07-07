import functools
import itertools
import operator
import time
import math

primes = []
prime_set = set()
lagged_fib_cache = [0]
linear_con_cache = [0]

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
def generate_primes_sieve(n, include_list=True, include_set=True):
	global prime_set
	primes.clear()
	primes.append(2)
	primes.append(3)
	primes.append(5)
	prime_set.add(2)
	prime_set.add(3)
	prime_set.add(5)
	prime_sieve = [False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True] * (n // 30 + 1)
	prime_sieve[1] = False
	for i in range(7, n):
		if prime_sieve[i]:
			if include_list:
				primes.append(i)
			if include_set:
				prime_set.add(i)
			for j in range(i, n, i):
				prime_sieve[j] = False

def is_prime(n):
	if n < 2:
		return False
	if n <= primes[-1]:
		return n in primes
	for p in primes:
		if n == p or p * p > n:
			return True
		elif n % p == 0:
			return False
	return True

def triangle(n):
	return (n * (n + 1)) // 2

def square(n):
	return n ** 2
	
def pentagon(n):
	return (n * (3 * n - 1)) // 2

def hexagon(n):
	return n * (2 * n - 1)

def heptagon(n):
	return (n * (5 * n - 3)) // 2

def octagon(n):
	return n * (3 * n - 2)

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

def flatten(list):
	return [item for sublist in list for item in sublist]

def sign(n):
	if n < 0:
		return -1
	elif n > 0:
		return 1
	else:
		return 0

def product(nums):
	return functools.reduce(operator.mul, nums, 1)

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def lagged_fibonacci(n):
	while n > 0:
		n -= 1
		k = len(lagged_fib_cache)
		if k <= 55:
			lagged_fib_cache.append(((100003 - 200003*k + 300007*k**3) % 1000000) - 500000)
		else:
			lagged_fib_cache.append(((lagged_fib_cache[k - 24] + lagged_fib_cache[k - 55] + 1000000) % 1000000) - 500000)

def linear_congruential(n):
	t = 0
	for n in range(1, n + 1):
		t = (615949*t + 797807) % 2**20
		linear_con_cache.append(t - 2**19)
			
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