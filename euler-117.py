# Solution to https://projecteuler.net/problem=117

import utilities

cache = dict()

def count_tile_combos(n, m_min, m_max):
	if (n, m_min, m_max) in cache:
		return cache[(n, m_min, m_max)]
	total = 1
	for length in range(m_min, m_max + 1):
		for pos in range(0, n - length + 1):
			total += count_tile_combos(n - (pos + length), m_min, m_max)
	cache[(n, m_min, m_max)] = total
	return total

def main():
	return count_tile_combos(50, 2, 4)

if __name__ == "__main__":
	utilities.print_runtime(main)