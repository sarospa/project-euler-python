# Solution to https://projecteuler.net/problem=35

import utilities

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	count = 0
	for p in prime_set:
		rotations = {int(str(p)[i:] + str(p)[:i]) for i in range(1, len(str(p)))}
		if rotations & prime_set == rotations:
			count += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)