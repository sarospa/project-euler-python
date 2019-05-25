# Solution to https://projecteuler.net/problem=141

import math
import itertools
import utilities as utils

MAX = 10**6

def divisor_sieve(n):
	sieve = [set([i]) for i in range(n + 1)]
	for i in range(2, int(math.sqrt(n)) + 1):
		sieve[i**2].add(i)
		for j in range(i**2 + i, n + 1, i):
			sieve[j].add(i)
			sieve[j].add(j // i)
	return sieve

def main():
	squares = {n**2 for n in range(1, MAX)}
	hits = set()
	sieve = divisor_sieve(MAX)
	for d in range(len(sieve)):
		sq_sieve = {num for num in {utils.product(pair) for pair in itertools.product(sieve[d], repeat=2)} | sieve[d] if num > d and num < MAX}
		for q in sq_sieve:
			r = d**2 // q
			n = d * q + r
			if n in squares:
				hits.add(n)
	return sum(hits)

if __name__ == "__main__":
	utils.print_runtime(main)