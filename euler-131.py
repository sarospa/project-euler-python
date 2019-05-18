# Solution to https://projecteuler.net/problem=131

import itertools
import utilities as utils

MAX = 1000000

def main():
	utils.generate_primes_sieve(MAX)
	count = 0
	found_index = -1
	upper_bound_multiplier = 10
	for n_root in itertools.count(1):
		if n_root**2 * upper_bound_multiplier > MAX:
			break
		for i in range(found_index + 1, len(utils.primes)):
			if utils.primes[i] > n_root**2 * upper_bound_multiplier:
				break
			n = n_root**3
			p = utils.primes[i]
			val = n**3 + n**2 * p
			root = int(round(val**(1/3)))
			if root**3 == val:
				count += 1
				upper_bound_multiplier = p / n_root**2
				found_index = i
				break
	return count

if __name__ == "__main__":
	utils.print_runtime(main)