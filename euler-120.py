# Solution to https://projecteuler.net/problem=120

import itertools
import utilities

def main():
	total = 0
	for a in range(3, 1001):
		max_val = 0
		a_sq = a**2
		b = a - 1
		c = a + 1
		for n in range(2, a*2 + 2):
			b *= a - 1
			c *= a + 1
			val = (b + c) % a_sq
			if val > max_val:
				max_val = val
		total += max_val
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)