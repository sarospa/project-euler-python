# Solution to https://projecteuler.net/problem=95

import math
import utilities

MAX = 1000000

def divisor_sieve(n):
	sieve = [1] * (n + 1)
	for i in range(2, int(math.sqrt(n)) + 1):
		sieve[i**2] += i
		for j in range(i**2 + i, n + 1, i):
			sieve[j] += i + (j // i)
	return sieve

def main():
	sums = divisor_sieve(MAX)
	all_chains = set()
	best_chain = []
	for i in range(len(sums)):
		if i not in all_chains:
			cur_chain = []
			chain_index = i
			while chain_index not in cur_chain and chain_index <= MAX:
				cur_chain.append(chain_index)
				chain_index = sums[chain_index]
			if chain_index in cur_chain:
				amicable_chain = cur_chain[cur_chain.index(chain_index):]
				if len(amicable_chain) > len(best_chain):
					best_chain = amicable_chain
			all_chains |= set(cur_chain)
	return sorted(best_chain)[0]

if __name__ == "__main__":
	utilities.print_runtime(main)