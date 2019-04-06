# Solution to https://projecteuler.net/problem=21

import utilities
import math

def sum_divisors(n):
	divisors = set()
	for j in range(2, round(math.sqrt(n) + 1)):
		if n % j == 0:
			divisors.add(j)
			divisors.add(n // j)
	return sum(divisors) + 1

def main():
	n = 0
	for i in range(1, 10000):
		j = sum_divisors(i)
		if i != j and sum_divisors(j) == i:
			n += i
	print(n)

utilities.print_runtime(main)