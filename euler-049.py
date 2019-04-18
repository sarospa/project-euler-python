# Solution to https://projecteuler.net/problem=49

import utilities

def main():
	utilities.generate_primes_sieve(10000)
	prime_set = set(utilities.primes)
	for p2 in [p2 for p2 in utilities.primes if p2 > 999]:
		if p2 == 4817:
			continue
		for i in range(1, 10000):
			if p2 - i < 1000 or p2 + i > 9999:
				break
			p1 = p2 - i
			p3 = p2 + i
			if p1 in prime_set and p2 in prime_set and p3 in prime_set and sorted(str(p1)) == sorted(str(p2)) and sorted(str(p3)) == sorted(str(p2)):
				return str(p1) + str(p2) + str(p3)

if __name__ == "__main__":
	utilities.print_runtime(main)