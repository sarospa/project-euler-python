# Solution to https://projecteuler.net/problem=137

import itertools
import math
import utilities as utils

def main():
	count = 0
	prev = 1
	setup = True
	n = 1
	while True:
		val = 1 + 2*n + 5*n**2
		if val == int(math.sqrt(val))**2:
			count += 1
			ratio = n / prev
			if prev != 1:
				setup = False
			prev = n
			if count == 15:
				return n
			if not setup:
				n = int(n * ratio)
		if setup:
			n += 1
		else:
			n -= 1

if __name__ == "__main__":
	utils.print_runtime(main)