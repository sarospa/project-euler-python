# Solution to https://projecteuler.net/problem=110

import itertools
import math
import utilities

TARGET = 4000000

def gen_from_sq_factors(factors):
	return utilities.product([utilities.primes[index]**((count - 1) // 2) for index, count in enumerate(factors)])

def main():
	utilities.generate_primes_sieve(1000000)
	upper_bound_range = int(math.log(TARGET * 2, 3)) + 1
	upper_bound = utilities.product([utilities.primes[i] for i in range(int(math.log(TARGET * 2, 3)) + 1)])
	factors_list = [3]
	while True:
		n = gen_from_sq_factors(factors_list)
		solutions = (utilities.product(factors_list) + 1) // 2
		if solutions > TARGET and n < upper_bound:
			upper_bound = n
		if len(factors_list) >= upper_bound_range:
			return upper_bound
		if n > upper_bound or solutions > TARGET:
			for i in range(len(factors_list)):
				if factors_list[i] > 3:
					factors_list[i] = 3
					if i == len(factors_list) - 1:
						factors_list.append(3)
					else:
						factors_list[i + 1] += 2
					break
			else:
				return upper_bound
		else:
			factors_list[0] += 2

if __name__ == "__main__":
	utilities.print_runtime(main)