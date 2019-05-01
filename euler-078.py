# Solution to https://projecteuler.net/problem=78

import itertools
import utilities

cache = {0:1}

def partitions(n):
	if n < 0:
		return 0
	if n in cache:
		return cache[n]
	sign = 1
	result = 0
	for k in itertools.count(1):
		t_pos = partitions(n - k * (3 * k - 1) // 2)
		t_neg = partitions(n - (-k) * (3 * (-k) - 1) // 2)
		result += sign * (t_pos + t_neg)
		sign *= -1
		if t_pos == 0 or t_neg == 0:
			break
	cache[n] = result
	return cache[n]

def main():
	for n in itertools.count(1):
		result = partitions(n)
		if result % 1000000 == 0:
			return n

if __name__ == "__main__":
	utilities.print_runtime(main)