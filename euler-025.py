# Solution to https://projecteuler.net/problem=25

import utilities

def main():
	f1 = 1
	f2 = 1
	index = 2
	while len(str(f2)) < 1000:
		f2 = f1 + f2
		f1 = f2 - f1
		index += 1
	print(index)

utilities.print_runtime(main)