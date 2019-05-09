# Solution to 

import utilities

cache = dict()

def count_block_combos(n):
	if n in cache:
		return cache[n]
	total = 1
	for length in range(3, n + 1):
		for pos in range(0, n - length + 1):
			total += count_block_combos(n - (pos + length + 1))
	cache[n] = total
	return total

def main():
	return count_block_combos(50)

if __name__ == "__main__":
	utilities.print_runtime(main)