# Solution to https://projecteuler.net/problem=31

import utilities

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
MAX = 200
cache = dict()

def count_combos(index, total):
	if (index, total) in cache:
		return cache[(index, total)]
	if index >= len(COINS):
		return 0
	count = 0
	for remaining in range(total, -1, -COINS[index]):
		if remaining == 0:
			count += 1
		else:
			count += count_combos(index + 1, remaining)
	cache[(index, total)] = count
	return count

def main():
	return count_combos(0, MAX)

if __name__ == "__main__":
	utilities.print_runtime(main)