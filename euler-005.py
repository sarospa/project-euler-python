# Solution to https://projecteuler.net/problem=5

import utilities

def main():
	n = 1
	for i in range(1, 21):
		temp_n = n
		temp_i = i
		for j in range(2, i + 1):
			while temp_i % j == 0 and temp_n % j == 0:
				temp_n = temp_n // j
				temp_i = temp_i // j
		n = n * temp_i
	print(n)

utilities.print_runtime(main)