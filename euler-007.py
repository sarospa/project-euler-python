# Solution to https://projecteuler.net/problem=7

import utilities

def main():
	utilities.generate_primes(10000)
	print(utilities.primes[10000])

utilities.print_runtime(main)