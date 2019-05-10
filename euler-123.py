# Solution to https://projecteuler.net/problem=123

import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	for i in range(0, len(utilities.primes), 2):
		n = i + 1
		r = utilities.primes[i] * n * 2
		if r > 10**10:
			return n

if __name__ == "__main__":
	utilities.print_runtime(main)