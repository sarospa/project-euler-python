# Solution to https://projecteuler.net/problem=124

import utilities

prime_set = set()

def radicals(n):
	total = 1
	for p in utilities.primes:
		if n in prime_set:
			return total * n
		if p * p > n:
			return total
		if n % p == 0:
			total *=p
			while n % p == 0:
				n //= p
	return total

def main():
	global prime_set
	utilities.generate_primes_sieve(100000)
	prime_set = set(utilities.primes)
	return sorted([(radicals(n), n) for n in range(1, 100001)])[9999][1]

if __name__ == "__main__":
	utilities.print_runtime(main)