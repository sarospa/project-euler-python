# Solution to https://projecteuler.net/problem=111

import itertools
import utilities

DIGITS = 10

def main():
	utilities.generate_primes_sieve(100000)
	total = 0
	for d in range(10):
		base = list(itertools.repeat(str(d), DIGITS))
		digit_total = 0
		for i in range(1, DIGITS):
			index_combos = list(itertools.combinations(range(DIGITS), i))
			digit_groups = list(itertools.product("0123456789", repeat=i))
			for combo in index_combos:
				for group in digit_groups:
					p = base.copy()
					for j in range(i):
						p[combo[j]] = group[j]
					p = int(''.join(p))
					if len(str(p)) == DIGITS and utilities.is_prime(p):
						digit_total += p
			if digit_total > 0:
				break
		total += digit_total
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)