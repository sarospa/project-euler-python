# Solution to https://projecteuler.net/problem=145

import itertools
import utilities as utils

MAX = 9

def main():
	even_carry = 0
	odd_carry = 0
	even_no_carry = 0
	odd_no_carry = 0
	even_zero = 0
	odd_zero = 0
	digit_pairs = {(int(pair[0]), int(pair[1])) for pair in itertools.product("0123456789", repeat=2)}
	for pair in digit_pairs:
		pair_sum = sum(pair)
		if pair_sum % 2 == 0:
			if pair_sum >= 10:
				even_carry += 1
			elif pair[0] == 0 or pair[1] == 0:
				even_zero += 1
			else:
				even_no_carry += 1
		else:
			if pair_sum >= 10:
				odd_carry += 1
			elif pair[0] == 0 or pair[1] == 0:
				odd_zero += 1
			else:
				odd_no_carry += 1
	total = 0
	for k in range(1, MAX + 1):
		if k % 2 == 0:
			total += (odd_no_carry + odd_zero)**(k//2 - 1) * odd_no_carry 
		elif k % 4 == 3:
			total += odd_carry**(k//4 + 1) * (even_no_carry + even_zero)**(k//4) * 5
	return total

if __name__ == "__main__":
	utils.print_runtime(main)