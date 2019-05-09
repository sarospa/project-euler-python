# Solution to https://projecteuler.net/problem=119

import itertools
import math
import utilities

def digit_power_sum(n, exp):
	return sum([int(digit) for digit in str(n**exp)])

def main():
	terms = set()
	upper_bound = math.inf
	for n in itertools.count(2):
		for exp in range(2, 101):
			#print(n, exp)
			sum_val = digit_power_sum(n, exp)
			if sum_val == n and n**exp < upper_bound:
				terms.add(n**exp)
			if n**exp > upper_bound:
				break
		if len(terms) >= 100:
			break
	return sorted(terms)[29]

if __name__ == "__main__":
	utilities.print_runtime(main)