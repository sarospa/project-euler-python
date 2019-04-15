# Solution to https://projecteuler.net/problem=30

import utilities

def sum_of_digit_powers(n, power):
	return sum([int(ch) ** power for ch in str(n)])

def main():
	total = 0
	for i in range(2, 1000000):
		if i == sum_of_digit_powers(i, 5):
			total += i
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)