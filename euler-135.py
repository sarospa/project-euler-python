# Solution to https://projecteuler.net/problem=135

import itertools
import math
import utilities as utils

TARGET = 1000000

def main():
	counts = [0] * TARGET
	for i in itertools.count(2, 2):
		floor = int(math.ceil(math.sqrt(max(i**2 - (TARGET - 1), 0))))
		if floor == i:
			break
		for j in range(floor, i):
			a = i // 2
			n = i**2 - j**2
			x = (-6 * a + 2 * j) // -2
			if x - 2 * a > 0:
				counts[n] += 1
			x = (-6 * a - 2 * j) // -2
			if x - 2 * a > 0 and j != 0:
				counts[n] += 1
	return len([count for count in counts if count == 10])

if __name__ == "__main__":
	utils.print_runtime(main)