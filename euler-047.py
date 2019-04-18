# Solution to https://projecteuler.net/problem=47

import itertools
import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	consecutives = 0
	for n in itertools.count(4):
		factors = 0
		n_temp = n
		for p in utilities.primes:
			if n_temp % p == 0:
				factors += 1
			while n_temp % p == 0:
				n_temp //= p
			if n_temp in prime_set:
				factors += 1
				break
			if n_temp == 1:
				break
		if factors == 4:
			consecutives += 1
		else:
			consecutives = 0
		if consecutives == 4:
			return n - 3

if __name__ == "__main__":
	utilities.print_runtime(main)