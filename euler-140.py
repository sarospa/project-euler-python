# Solution to https://projecteuler.net/problem=140

import math
import itertools
import utilities as utils

def main():
	n = 1
	hits = []
	while True:
		val = 5 * n**2 + 1 + 14 * n
		if val == int(math.sqrt(val))**2:
			hits.append(n)
			if len(hits) == 30:
				return sum(hits)
			if len(hits) > 2:
				n = int(n * hits[len(hits) - 2] / hits[len(hits) - 3])
		if len(hits) > 2:
			n -= 1
		else:
			n += 1

if __name__ == "__main__":
	utils.print_runtime(main)