# Solution to https://projecteuler.net/problem=58

import math
import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	prime_count = 0
	total_count = 1
	n = 1
	for i in range(2, 1000000, 2):
		for j in range(3):
			n += i
			total_count += 1
			if n in prime_set or utilities.is_prime(n):
				prime_count += 1
		n += i
		total_count += 1
		if prime_count * 10 < total_count:
			return i + 1

if __name__ == "__main__":
	utilities.print_runtime(main)