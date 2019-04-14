# Solution to https://projecteuler.net/problem=27

import utilities

MAX = 10000000

def main():
	utilities.generate_primes_sieve(MAX)
	prime_set = set(utilities.primes)
	largest_n = 0
	value = 0
	for a in range(-999, 1000):
		for b in range(-999, 1000):
			n = 0
			p = n**2 + a*n + b
			while p in prime_set:
				n += 1
				p = n**2 + a*n + b
			if n > largest_n:
				largest_n = n
				value = a * b
	print(value)

utilities.print_runtime(main)