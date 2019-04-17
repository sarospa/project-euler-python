# Solution to https://projecteuler.net/problem=40

import utilities

def main():
	index = 1
	value = 1
	target = 1
	product = 1
	while target <= 1000000:
		digits = str(value)
		if target >= index and target < index + len(digits):
			product *= int(digits[target - index])
			target *= 10
		value += 1
		index += len(digits)
	return product

if __name__ == "__main__":
	utilities.print_runtime(main)