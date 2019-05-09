# Solution to https://projecteuler.net/problem=118

import itertools
import utilities

all_digits = "123456789"

def find_sets(prime_groups, digits, index):
	if len(digits) == 0:
		return 1
	total = 0
	for i in range(index, len(prime_groups)):
		if set(prime_groups[i][0]) <= set(digits):
			total += prime_groups[i][1] * find_sets(prime_groups, ''.join(sorted(set(digits) - set(prime_groups[i][0]))), i + 1)
	return total

def main():
	utilities.generate_primes_sieve(100000)
	primes = sorted([''.join(p) for p in itertools.chain.from_iterable(itertools.permutations(all_digits, r) for r in range(1, len(all_digits)+1)) if utilities.is_prime(int(''.join(p)))], key=lambda x:sorted(x))
	prime_groups = [(''.join(k), len(list(g))) for k, g in itertools.groupby(primes, key=lambda x:sorted(x))]
	return find_sets(prime_groups, all_digits, 0)

if __name__ == "__main__":
	utilities.print_runtime(main)