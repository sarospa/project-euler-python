# Solution to https://projecteuler.net/problem=101

import math
import utilities

def polynomial(terms, n):
	total = 0
	for i in range(len(terms)):
		total += terms[i] * n**i
	return total

def fit_sequence(sequence):
	if len(sequence) == 1:
		return sequence
	degree = len(sequence) - 1
	diffs = sequence.copy()
	while len(diffs) > 1:
		new_diffs = []
		for i in range(len(diffs)-1):
			new_diffs.append(diffs[i+1] - diffs[i])
		diffs = new_diffs
	term = diffs[0] // math.factorial(degree)
	for i in range(len(sequence)):
		sequence[i] -= term * (i+1)**degree
	return fit_sequence(sequence[:-1]) + [term]

def main():
	big_poly = [1, -1] * 5 + [1]
	sequence = [polynomial(big_poly, i) for i in range(1, 11)]
	return sum([polynomial(poly, len(poly) + 1) for poly in [fit_sequence(sequence[:len(sequence)-i]) for i in range(10)]])

if __name__ == "__main__":
	utilities.print_runtime(main)