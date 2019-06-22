# Solution to https://projecteuler.net/problem=209

import utilities as utils

luc_cache = dict()

INPUTS = 6

def lucas(n):
	if n == 1:
		return 1
	elif n < 1:
		return 2
	if n in luc_cache:
		return luc_cache[n]
	luc_cache[n] = lucas(n - 1) + lucas(n - 2)
	return luc_cache[n]

def main():
	bits_mapping = [((i << 1) & (2**INPUTS - 1)) | (((i & 2**(INPUTS - 1)) >> (INPUTS - 1)) ^ (((i & 2**(INPUTS - 2)) >> (INPUTS - 2)) & ((i & 2**(INPUTS - 3)) >> (INPUTS - 3)))) for i in range(2**INPUTS)]
	bits_counted = [False] * 2**INPUTS
	total = 1
	lucas(2**INPUTS)
	for i in range(2**INPUTS):
		if not bits_counted[i]:
			j = i
			cycle_count = 0
			while not bits_counted[j]:
				cycle_count += 1
				bits_counted[j] = True
				j = bits_mapping[j]
			cycle_total = lucas(cycle_count)
			total *= cycle_total
	return total

if __name__ == "__main__":
	utils.print_runtime(main)