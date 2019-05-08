# Solution to https://projecteuler.net/problem=108

import itertools
import math
import utilities

TARGET = 1000

def main():
	best_count = 0
	for n in itertools.count(180, 180):
		count = 0
		for a in itertools.count(n + 1):
			if (n * a) % (a - n) == 0:
				count += 1
			if a > n * 2:
				break
		if count > TARGET:
			return n
		if count > best_count:
			best_count = count
			print((n, best_count))

if __name__ == "__main__":
	utilities.print_runtime(main)