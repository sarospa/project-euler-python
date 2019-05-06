# Solution to https://projecteuler.net/problem=100

from fractions import Fraction
import itertools
import math
import utilities

def main():
	prev = 1
	i = 2
	while True:
		denominator = int(round(i * math.sqrt(2)))
		frac_a = Fraction(i, denominator)
		frac_b = Fraction(i - 1, denominator - 1)
		if frac_a * frac_b == Fraction(1, 2):
			ratio = i / prev
			prev = i
			if denominator > 10**12:
				return i
			i = int(i * ratio)
		else:
			i += 1

if __name__ == "__main__":
	utilities.print_runtime(main)