# Solution to https://projecteuler.net/problem=132

import itertools
import math
import utilities as utils

prime_set = set()

def divisors(n):
	divisors = []
	for m in range(2, int(math.sqrt(n)) + 1):
		if n % m == 0:
			divisors.append(m)
			if n // m != n:
				divisors.append(n // m)
	return divisors

def prime_factors(n):
	factors = set()
	for p in utils.primes:
		if n in prime_set:
			factors.add(n)
			return factors
		if p * p > n:
			break
		if n % p == 0:
			factors.add(p)
			while n % p == 0:
				n //= p
	return factors

def main():
	global prime_set
	utils.generate_primes_sieve(162000)
	prime_set = set(utils.primes)
	divisors_list = sorted([1] + divisors(10**9))
	factors = set()
	prev_vals = set()
	for div in divisors_list:
		val = 10**div + 1
		val_factors = prime_factors(val)
		factors |= val_factors
		val = int("1" * div)
		prev_vals.add(val)
		val_factors = prime_factors(val)
		factors |= val_factors
		if len(factors) >= 40:
			break
	return sum(sorted(factors)[:40])

if __name__ == "__main__":
	utils.print_runtime(main)