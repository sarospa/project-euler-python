# Solution to https://projecteuler.net/problem=148

import utilities as utils

SIZE = 7
MAX = 10**9

def calc_triangle(height):
	if height < SIZE:
		return utils.triangle(height)
	count = SIZE
	total = utils.triangle(SIZE)
	while height >= count * SIZE:
		count *= SIZE
		total *= utils.triangle(SIZE)
	iterations = height // count
	return total * utils.triangle(iterations) + calc_triangle(height - count * iterations) * (iterations + 1)

def main():
	return calc_triangle(MAX)

if __name__ == "__main__":
	utils.print_runtime(main)