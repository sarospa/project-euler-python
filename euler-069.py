# Solution to https://projecteuler.net/problem=69

import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	totients = list(range(1000001))
	for p in utilities.primes:
		for n in range(p, 1000001, p):
			totients[n] = totients[n] * (p - 1) // p
	max_ratio = 0
	best_n = 0
	for n in range(1, 1000001):
		if n / totients[n] > max_ratio:
			max_ratio = n / totients[n]
			best_n = n
	return best_n

if __name__ == "__main__":
	utilities.print_runtime(main)