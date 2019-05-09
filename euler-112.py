# Solution to https://projecteuler.net/problem=112

import itertools
import utilities

def is_bouncy(n):
	last_digit = n % 10
	increase = False
	decrease = False
	n //= 10
	while n > 0:
		digit = n % 10
		if last_digit > digit:
			increase = True
		elif last_digit < digit:
			decrease = True
		n //= 10
		last_digit = digit
	return increase and decrease

def main():
	count = 0
	for i in itertools.count(1):
		if not is_bouncy(i):
			count += 1
		if count * 100 == i:
			return i

if __name__ == "__main__":
	utilities.print_runtime(main)