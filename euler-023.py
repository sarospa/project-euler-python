# Solution to https://projecteuler.net/problem=23

import utilities
import itertools

abundants = set()
non_sums = set(range(1, 28124))

def main():
	for i in range(1, 28124):
		if utilities.sum_divisors(i) > i:
			abundants.add(i)
	for pair in itertools.combinations_with_replacement(abundants, 2):
		non_sums.discard(sum(pair))
	return sum(non_sums)

if __name__ == "__main__":
	utilities.print_runtime(main)