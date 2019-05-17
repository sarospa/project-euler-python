# Solution to https://projecteuler.net/problem=127

from fractions import gcd
import itertools
import utilities

MAX = 120000

prime_set = set()

def prime_factors(n):
	factors = set()
	for p in utilities.primes:
		if n in prime_set:
			factors.add(n)
			return factors
		if p * p > n:
			return factors
		if n % p == 0:
			factors.add(p)
			while n % p == 0:
				n //= p
	return factors

def main():
	global prime_set
	utilities.generate_primes_sieve(MAX)
	prime_set = set(utilities.primes)
	factors_cache = []
	term_index = dict()
	total = 0
	for n in range(1, MAX):
		factors = prime_factors(n)
		factors_cache.append((utilities.product(factors), factors, n))
	factors_cache.sort()
	for i in range(len(factors_cache)):
		term_index[factors_cache[i][2]] = i
	for a in factors_cache:
		if a[0]**2 >= MAX:
			break
		for b in factors_cache[factors_cache.index(a) + 1:]:
			if a[0] * b[0] >= MAX:
				break
			if a[2] + b[2] >= MAX:
				continue
			c = factors_cache[term_index[a[2] + b[2]]]
			if len(a[1] | b[1] | c[1]) == len(a[1]) + len(b[1]) + len(c[1]) and a[0] * b[0] * c[0] < c[2]:
				total += c[2]
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)