# Solution to https://projecteuler.net/problem=57

import utilities

def main():
	count = 0
	for i in range(1, 1000):
		numerator = 1
		denominator = 2
		for j in range(i):
			numerator += denominator * 2
			temp = denominator
			denominator = numerator
			numerator = temp
		numerator += denominator
		if len(str(numerator)) > len(str(denominator)):
			count += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)