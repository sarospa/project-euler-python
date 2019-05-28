# Solution to https://projecteuler.net/problem=142

import itertools
import math
import utilities as utils

def main():
	matches_a = dict()
	matches_b = dict()
	for n in itertools.count(1):
		n_match = set()
		n_sq = n**2
		for m in range(2 - (n % 2), n, 2):
			m_sq = m**2
			x = (n_sq + m_sq) // 2
			y = (n_sq - m_sq) // 2
			if x in matches_a:
				for z in matches_a[x]:
					if max(y, z) in matches_a and min(y, z) in matches_a[max(y, z)]:
						return x + y + z
				matches_a[x].add(y)
			else:
				matches_a[x] = {y}
			if y in matches_b:
				matches_b[y].add(x)
			else:
				matches_b[y] = {x}
			if x in matches_b and y in matches_b and len(matches_b[x] & matches_b[y]) > 0:
				return x + y + sorted(matches_b[x] & matches_b[y])[0]

if __name__ == "__main__":
	utils.print_runtime(main)