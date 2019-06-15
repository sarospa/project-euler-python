# Solution to https://projecteuler.net/problem=146

import utilities as utils

MAX = 15*10**7

def is_prime_targets(n, targets):
	nonprime_targets = {target for target in targets if n + target not in utils.prime_set}
	if len(nonprime_targets) == 0:
		return True
	for p in utils.primes:
		mod_targets = {target % p for target in nonprime_targets}
		if p**2 > n + max(nonprime_targets):
			return True
		elif (p - (n % p)) % p in mod_targets:
			return False
	return True

def is_any_prime_targets(n, targets):
	targets_copy = targets.copy()
	prime_targets = {target for target in targets_copy if n + target in utils.prime_set}
	if len(prime_targets) > 0:
		return True
	for p in utils.primes:
		if len(targets_copy) == 0:
			return False
		if p**2 > n + max(targets_copy):
			return True
		targets_copy -= {target for target in targets_copy if (n + target) % p == 0}
	return len(targets_copy) == 0

def main():
	utils.generate_primes_sieve(MAX)
	targets = {1, 3, 7, 9, 13, 27}
	antitargets = {num for num in range(1, 27) if num not in targets}
	candidates = range(10, MAX, 10)
	for p in utils.primes:
		if p > 1000:
			break
		mod_targets = {target % p for target in targets}
		hits = {n for n in range(p) if p - (n**2 % p) not in mod_targets or n**2 + (p - (n**2 % p)) == p}
		candidates = {candidate for candidate in candidates if candidate % p in hits}
	total = 0
	for n in candidates:
		if is_prime_targets(n**2, targets) and not is_any_prime_targets(n**2, antitargets):
			total += n
	return total

if __name__ == "__main__":
	utils.print_runtime(main)