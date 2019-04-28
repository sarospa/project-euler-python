# Solution to https://projecteuler.net/problem=73

from fractions import Fraction
import math
import utilities

def main():
	lower_bound = Fraction(1, 3)
	upper_bound = Fraction(1, 2)
	count = 0
	for i in range(4, 12001):
		for j in range(i // 3 + 1, i // 2 + 1):
			if math.gcd(i, j) == 1:
				count += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)