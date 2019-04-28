# Solution to https://projecteuler.net/problem=74

import math
import utilities

chain_counts = {}

def digit_factorial(n):
	return sum([math.factorial(int(ch)) for ch in str(n)])

def calc_chain(n):
	if n in chain_counts:
		return chain_counts[n]
	else:
		factorial = digit_factorial(n)
		if factorial == n:
			chain_counts[n] = 1
		else:
			chain_counts[n] = 1 + calc_chain(digit_factorial(n))
		return chain_counts[n]

def main():
	chain_counts[169] = 3
	chain_counts[363601] = 3
	chain_counts[1454] = 3
	chain_counts[871] = 2
	chain_counts[45361] = 2
	chain_counts[872] = 2
	chain_counts[45362] = 2
	for n in range(2, 1000000):
		calc_chain(n)
	return len([n for (i,n) in chain_counts.items() if i < 1000000 and n == 60])

if __name__ == "__main__":
	utilities.print_runtime(main)