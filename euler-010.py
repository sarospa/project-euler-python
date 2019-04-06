# Solution to https://projecteuler.net/problem=10

import utilities

def main():
	utilities.generate_primes_sieve(2000000)
	print(sum(utilities.primes))

utilities.print_runtime(main)