# Solution to https://projecteuler.net/problem=46

import itertools
import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	for n in itertools.count(9, 2):
		if n not in prime_set:
			found = False
			for p in {p for p in prime_set if p < n}:
				m = 1
				while p + (2 * m**2) < n:
					m += 1
				if p + (2 * m**2) == n:
					found = True
					break
			if not found:
				return n

if __name__ == "__main__":
	utilities.print_runtime(main)