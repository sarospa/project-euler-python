# Solution to https://projecteuler.net/problem=115

import itertools
import utilities

cache = dict()

def count_block_combos(n, m):
	if (n, m) in cache:
		return cache[(n, m)]
	total = 1
	for length in range(m, n + 1):
		for pos in range(0, n - length + 1):
			total += count_block_combos(n - (pos + length + 1), m)
	cache[(n, m)] = total
	return total

def main():
	for n in itertools.count(50):
		if count_block_combos(n, 50) > 1000000:
			return n

if __name__ == "__main__":
	utilities.print_runtime(main)