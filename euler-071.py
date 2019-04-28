# Solution to https://projecteuler.net/problem=71

from fractions import Fraction
import math
import utilities

def main():
	closest = Fraction(0, 1)
	target = Fraction(3, 7)
	numerator = 0
	denominator = 1
	while denominator <= 1000000:
		current = Fraction(numerator, denominator)
		if current > target:
			denominator += 1
		else:
			numerator += 1
			if current > closest and current < target:
				closest = current
	return closest.numerator

if __name__ == "__main__":
	utilities.print_runtime(main)