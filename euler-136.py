# Solution to https://projecteuler.net/problem=136

import itertools
import utilities as utils

TARGET = 50000000

def main():
	utils.generate_primes_sieve(TARGET)
	count = 2
	for p in utils.primes[1:]:
		if p * 16 < TARGET:
			count += 1
		if p * 4 < TARGET:
			count += 1
		if (p + 1) % 4 == 0:
			count += 1
	return count

if __name__ == "__main__":
	utils.print_runtime(main)