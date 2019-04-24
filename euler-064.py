# Solution to https://projecteuler.net/problem=64

import math
import utilities

def calc_period(n):
	terms = []
	nearest = int(math.sqrt(n))
	term = nearest
	numerator = 1
	denominator = term
	terms.append((term, numerator, denominator))
	while True:
		new_numerator = denominator
		new_denominator = (n - denominator**2) // numerator
		term = (new_numerator + nearest) // new_denominator
		denominator = nearest - ((new_numerator + nearest) % new_denominator)
		numerator = new_denominator
		if (term, numerator, denominator) in terms:
			return len(terms) - terms.index((term, numerator, denominator))
		else:
			terms.append((term, numerator, denominator))

def main():
	count = 0
	for n in range(2, 10001):
		if int(math.sqrt(n))**2 != n and calc_period(n) % 2 == 1:
			count += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)