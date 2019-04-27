# Solution to https://projecteuler.net/problem=70

import math
import utilities

def main():
	utilities.generate_primes_sieve(10000000)
	totients = list(range(10000000))
	for p in utilities.primes:
		for n in range(p, 10000000, p):
			totients[n] = totients[n] * (p - 1) // p
	min_ratio = math.inf
	best_n = 0
	for n in range(2, 10000000):
		if n / totients[n] < min_ratio and sorted(str(n)) == sorted(str(totients[n])):
			min_ratio = n / totients[n]
			best_n = n
	return best_n

if __name__ == "__main__":
	utilities.print_runtime(main)