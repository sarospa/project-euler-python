# Solution to https://projecteuler.net/problem=60

import utilities

def match_in_group(group, p, prime_set):
	for p2 in group:
		if int(str(p) + str(p2)) not in prime_set or int(str(p2) + str(p)) not in prime_set:
			return False
	return True

def main():
	utilities.generate_primes_sieve(100000000)
	prime_set = set(utilities.primes)
	small_prime_set = {p for p in utilities.primes if p < 10000}
	groups = [[p1, p2] for p1 in small_prime_set for p2 in small_prime_set if p1 < p2 and match_in_group([p1], p2, prime_set)]
	groups = [group + [p] for p in small_prime_set for group in groups if p > max(group) and match_in_group(group, p, prime_set)]
	groups = [group + [p] for p in small_prime_set for group in groups if p > max(group) and match_in_group(group, p, prime_set)]
	groups = [group + [p] for p in small_prime_set for group in groups if p > max(group) and match_in_group(group, p, prime_set)]
	return sum(groups[0])

if __name__ == "__main__":
	utilities.print_runtime(main)