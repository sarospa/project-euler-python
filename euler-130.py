# Solution to https://projecteuler.net/problem=130

import itertools
import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	total = 0
	total_count = 0
	for i in itertools.count(10, 10):
		for n in [i + 1, i + 3, i + 7, i + 9]:
			if n not in prime_set:
				remainder = 1
				count = 1
				while remainder != 0:
					remainder = (remainder * 10 + 1) % n
					count += 1
				if (n - 1) % count == 0:
					total += n
					total_count += 1
					if total_count == 25:
						return total

if __name__ == "__main__":
	utilities.print_runtime(main)