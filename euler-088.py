# Solution to https://projecteuler.net/problem=88

import functools
import itertools
import operator
import utilities

def product(nums):
	return functools.reduce(operator.mul, nums, 1)

def factor_groups(vals):
	if len(vals) == 1:
		return (vals,)
	smaller = factor_groups(vals[:len(vals)-1])
	vals_partitioned = set()
	last_val = vals[len(vals)-1]
	for group in smaller:
		for i in range(len(group)):
			added_group = group[:i] + (group[i] * last_val,) + group[i+1:]
			vals_partitioned.add(tuple(sorted(added_group)))
		added_group = group + (last_val,)
		vals_partitioned.add(tuple(sorted(added_group)))
	return vals_partitioned

def prime_factors(n):
	factors = []
	for p in utilities.primes:
		while n % p == 0:
			factors.append(p)
			n //= p
	return factors

def main():
	total = 0
	unclaimed_ks = set(range(2, 12001))
	utilities.generate_primes_sieve(100000)
	for n in itertools.count(2):
		factors = prime_factors(n)
		factor_combos = [nums for nums in factor_groups(tuple(factors)) if len(nums) >= 2]
		k_val_found = False
		for combo in factor_combos:
			k_val = (n - sum(combo)) + len(combo)
			if k_val in unclaimed_ks:
				unclaimed_ks.remove(k_val)
				k_val_found = True
		if k_val_found:
			total += n
		if len(unclaimed_ks) == 0:
			break
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)