# Solution to https://projecteuler.net/problem=39

import utilities
import math

def main():
	counts = [0] * 1001
	for a in range(1, 1001):
		for b in range(a, 1001 - a):
			c = int(math.sqrt(a**2 + b**2))
			if c**2 == a**2 + b**2 and a + b + c <= 1000:
				counts[a + b + c] += 1
	return counts.index(max(counts))

if __name__ == "__main__":
	utilities.print_runtime(main)