# Solution to https://projecteuler.net/problem=7

import utilities

def main():
	utilities.generate_primes(10000)
	return utilities.primes[10000]

if __name__ == "__main__":
	utilities.print_runtime(main)