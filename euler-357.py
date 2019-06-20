# Solution to https://projecteuler.net/problem=357

import utilities as utils

MAX = 10**8

def main():
	utils.generate_primes_sieve(MAX, include_list=False)
	candidates = {p - 1 for p in utils.prime_set}
	for n in range(1, MAX + 1):
		if n not in utils.prime_set:
			for m in range(1, n):
				prod = m * (n - m)
				if prod > MAX:
					break
				candidates.discard(prod)
	return sum(candidates)

if __name__ == "__main__":
	utils.print_runtime(main)