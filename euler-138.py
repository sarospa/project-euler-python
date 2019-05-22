# Solution to https://projecteuler.net/problem=138

import math
import itertools
import utilities as utils

def main():
	count = 0
	total = 0
	prev = 1
	l = 2
	while True:
		approx_b = math.sqrt(4/5 * l**2)
		b = int(round(approx_b / 2)) * 2
		if abs(math.sqrt(l**2 - (b // 2)**2) - b) == 1:
			count += 1
			total += l
			ratio = l / prev
			prev = l
			l = int(l * ratio)
			if count == 12:
				return total
		else:
			l += 1

if __name__ == "__main__":
	utils.print_runtime(main)