# Solution to https://projecteuler.net/problem=14

import utilities

collatz_values = {}

def collatz(n):
	t = n
	terms = 1
	while t > 1:
		if t % 2 == 0:
			t = t // 2
		else:
			t = 3 * t + 1
		if t in collatz_values:
			collatz_values[n] = collatz_values[t] + terms
			return collatz_values[n]
		terms = terms + 1
	collatz_values[n] = terms
	return terms

def main():
	n = 1
	terms = 0
	for i in range(1, 1000000):
		next_terms = collatz(i)
		if next_terms > terms:
			n = i
			terms = next_terms
	return n

if __name__ == "__main__":
	utilities.print_runtime(main)