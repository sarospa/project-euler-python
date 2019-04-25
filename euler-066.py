# Solution to https://projecteuler.net/problem=66

import itertools
import math
import utilities

def continued_fraction(n):
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
			period_start = terms.index((term, numerator, denominator))
			return itertools.chain([term[0] for term in terms[:period_start]], itertools.cycle([term[0] for term in terms[period_start:]]))
		else:
			terms.append((term, numerator, denominator))

def calc_convergent(cont_fraction):
	numerator = cont_fraction[len(cont_fraction) - 1]
	denominator = 1
	for i in range(len(cont_fraction) - 2, -1, -1):
		temp = numerator
		numerator = denominator
		denominator = temp
		numerator += denominator * cont_fraction[i]
	return (numerator, denominator)

def main():
	largest_x = 0
	best_d = 0
	for d in range(2, 1001):
		if int(math.sqrt(d))**2 == d:
			continue
		fraction_terms = continued_fraction(d)
		finite_terms = []
		for term in fraction_terms:
			finite_terms.append(term)
			convergent = calc_convergent(finite_terms)
			result = convergent[0]**2 - d * convergent[1]**2
			if result == 1:
				if convergent[0] > largest_x:
					largest_x = convergent[0]
					best_d = d
				break
	return best_d

if __name__ == "__main__":
	utilities.print_runtime(main)