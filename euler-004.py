# Solution to https://projecteuler.net/problem=4

import utilities

def main():
	n = 0
	for i in range(100, 1000):
		for j in range(i, 1000):
			sum = i * j
			if utilities.is_palindrome(sum) and sum > n:
				n = sum
	print(n)

utilities.print_runtime(main)