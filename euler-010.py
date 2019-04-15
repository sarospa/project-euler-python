# Solution to https://projecteuler.net/problem=10

import utilities

def main():
	utilities.generate_primes_sieve(2000000)
	return sum(utilities.primes)

if __name__ == "__main__":
	utilities.print_runtime(main)