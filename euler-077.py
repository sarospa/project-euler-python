# Solution to https://projecteuler.net/problem=77

import utilities

cache = dict()

def count_combos(index, total, values):
	if (index, total) in cache:
		return cache[(index, total)]
	if index >= len(values):
		return 0
	count = 0
	for remaining in range(total, -1, -values[index]):
		if remaining == 0:
			count += 1
		else:
			count += count_combos(index + 1, remaining, values)
	cache[(index, total)] = count
	return count

def main():
	utilities.generate_primes_sieve(1000000)
	for n in range(1, 1000000):
		cache.clear()
		count = count_combos(0, n, [p for p in utilities.primes if p < n])
		if count > 5000:
			return n

if __name__ == "__main__":
	utilities.print_runtime(main)