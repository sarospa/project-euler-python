# Solution to https://projecteuler.net/problem=133

from fractions import gcd
import itertools
import utilities as utils

def main():
	utils.generate_primes_sieve(100000)
	total = 5
	for p in utils.primes[2:]:
		prev_result = -1
		for n in itertools.count(1):
			result = 10**gcd(10**n, p - 1) % p
			if prev_result == result:
				if result == 1:
					pass
				else:
					total += p
				break
			else:
				prev_result = result
	return total

if __name__ == "__main__":
	utils.print_runtime(main)