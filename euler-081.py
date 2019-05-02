# Solution to https://projecteuler.net/problem=81

import math
import utilities

matrix = []
cache = []

def calc_path(x, y):
	if x < 0 or y < 0:
		return math.inf
	if x == 0 and y == 0:
		cache[y][x] = matrix[y][x]
		return cache[y][x]
	if cache[y][x] is not None:
		return cache[y][x]
	min_sum = min(calc_path(x - 1, y), calc_path(x, y - 1)) + matrix[y][x]
	cache[y][x] = min_sum
	return cache[y][x]

def main():
	with open("euler-081-data.txt") as f:
		for line in f.readlines():
			dataline = []
			for num in line.split(","):
				dataline.append(int(num))
			matrix.append(dataline)
			cache.append([None] * len(dataline))
	return calc_path(len(matrix[0]) - 1, len(matrix) - 1)

if __name__ == "__main__":
	utilities.print_runtime(main)