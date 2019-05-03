# Solution to https://projecteuler.net/problem=87

import utilities

MAX = 50000000

def main():
	utilities.generate_primes_sieve(1000000)
	sums = set()
	for p1 in utilities.primes:
		if p1**4 > MAX:
			break
		for p2 in utilities.primes:
			if p1**4 + p2**3 > MAX:
				break
			for p3 in utilities.primes:
				if p1**4 + p2**3 + p3**2 > MAX:
					break
				sums.add(p1**4 + p2**3 + p3**2)
	return len(sums)

if __name__ == "__main__":
	utilities.print_runtime(main)