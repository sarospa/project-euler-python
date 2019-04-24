# Solution to https://projecteuler.net/problem=65

import utilities

def main():
	cont_fraction = [2]
	for i in range(1, 34):
		cont_fraction += [1, i * 2, 1]
	numerator = cont_fraction[len(cont_fraction) - 1]
	denominator = 1
	for i in range(len(cont_fraction) - 2, -1, -1):
		temp = numerator
		numerator = denominator
		denominator = temp
		numerator += denominator * cont_fraction[i]
	return sum([int(ch) for ch in str(numerator)])

if __name__ == "__main__":
	utilities.print_runtime(main)