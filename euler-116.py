# Solution to https://projecteuler.net/problem=116

import utilities

cache = dict()

def count_tile_combos(n, m):
	if (n, m) in cache:
		return cache[(n, m)]
	total = 0
	for pos in range(0, n - m + 1):
		total += count_tile_combos(n - (pos + m), m) + 1
	cache[(n, m)] = total
	return total

def main():
	return count_tile_combos(50, 2) + count_tile_combos(50, 3) + count_tile_combos(50, 4)

if __name__ == "__main__":
	utilities.print_runtime(main)