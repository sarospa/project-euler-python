# Solution to https://projecteuler.net/problem=143

from fractions import Fraction
from fractions import gcd
import itertools
import math
import utilities as utils

MAX = 120000

def main():
	squares = set()
	for x in itertools.count(1):
		square = x**2
		if square > 3*MAX**2:
			break
		squares.add(square)
	pairs = dict()
	matches = set()
	for k in range(1, MAX):
		for j in range(k + 1, min(2*k, MAX)):
			x = j**2 - k**2
			y = j * (2*k - j)
			divisor = math.gcd(x, y)
			x //= divisor
			y //= divisor
			if x + y > MAX:
				break
			for mul in itertools.count(1):
				x_mul = x * mul
				y_mul = y * mul
				if x_mul + y_mul <= MAX:
					if x_mul in pairs:
						pairs[x_mul].add(y_mul)
					else:
						pairs[x_mul] = set([y_mul])
					if y_mul in pairs:
						pairs[y_mul].add(x_mul)
					else:
						pairs[y_mul] = set([x_mul])
				else:
					break
	for p in pairs:
		for r in pairs[p]:
			for q in pairs[r] & pairs[p]:
				if p + q + r <= MAX:
					matches.add(p + q + r)
	return sum(matches)

if __name__ == "__main__":
	utils.print_runtime(main)