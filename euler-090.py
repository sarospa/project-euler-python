# Solution to https://projecteuler.net/problem=90

import itertools
import utilities

def check_digit(die, digit):
	return digit in die or (digit == 6 and 9 in die) or (digit == 9 and 6 in die)

def check_pair(die_1, die_2, num):
	digit_1 = num % 10
	digit_2 = num // 10
	return (check_digit(die_1, digit_1) and check_digit(die_2, digit_2)) or (check_digit(die_1, digit_2) and check_digit(die_2, digit_1))

def main():
	total = 0
	dice = list(itertools.combinations((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 6))
	squares = [i**2 for i in range(1, 10)]
	for die_1 in dice:
		for die_2 in dice[:dice.index(die_1) + 1]:
			match = True
			for num in squares:
				if not check_pair(die_1, die_2, num):
					match = False
					break
			if match:
				total += 1
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)