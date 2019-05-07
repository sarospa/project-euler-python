# Solution to https://projecteuler.net/problem=169

import itertools
import math
import utilities

TARGET = 10**25

cache = dict()

def calc_power_sums(n):
	t = 2**int(math.log2(n))
	total = 0
	while t * 4 - 2 >= n:
		total += calc_power_sums_rec(n, t)
		t //= 2
	return total

def calc_power_sums_rec(n, t, used = False):
	if (n, t, used) in cache:
		return cache[(n, t, used)]
	if n - t == 0:
		return 1
	if n - t < 0:
		return 0
	total = 0
	next_n = n - t
	if not used:
		total += calc_power_sums_rec(next_n, t, True)
	next_t = t
	while next_t * 4 - 2 >= next_n:
		next_t //= 2
		total += calc_power_sums_rec(next_n, next_t, False)
	cache[(n, t, used)] = total
	return total

def main():
	return calc_power_sums(TARGET)

if __name__ == "__main__":
	utilities.print_runtime(main)