# Solution to https://projecteuler.net/problem=41

import utilities

def main():
	utilities.generate_primes_sieve(10000000)
	for p in reversed(utilities.primes):
		if set(str(p)) == {str(digit) for digit in range(1, len(str(p)) + 1)}:
			return p

if __name__ == "__main__":
	utilities.print_runtime(main)