# Solution to https://projecteuler.net/problem=72

import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	totients = list(range(1000001))
	totients[1] = 0
	for p in utilities.primes:
		for n in range(p, 1000001, p):
			totients[n] = totients[n] * (p - 1) // p
	return sum(totients)

if __name__ == "__main__":
	utilities.print_runtime(main)