# Solution to https://projecteuler.net/problem=134

import itertools
import utilities as utils

TARGET = 1000000

def solve_congruence(mod_by, a):
	if a == 1:
		return (0, 1)
	multiple = mod_by // a
	remainder = mod_by % a
	next_result = solve_congruence(a, remainder)
	return (next_result[1], next_result[0] + next_result[1] * -multiple)

def main():
	utils.generate_primes_sieve(TARGET + 500)
	total = 0
	for i in range(2, len(utils.primes)):
		p1 = utils.primes[i]
		p2 = utils.primes[i+1]
		if p1 > TARGET:
			break
		mod_val = p2 - (10**len(str(p1)) % p2)
		result = solve_congruence(p2, mod_val)[1] * p1 % p2
		total += result * 10**len(str(p1)) + p1
	return total

if __name__ == "__main__":
	utils.print_runtime(main)