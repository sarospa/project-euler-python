# Solution to https://projecteuler.net/problem=15

import utilities

grid = [[0] * 21 for i in range(21)]

def calc_paths(x, y):
	if x == 0 or y == 0:
		grid[y][x] = 1
		return 1
	if grid[y - 1][x] == 0:
		calc_paths(x, y - 1)
	if grid[y][x - 1] == 0:
		calc_paths(x - 1, y)
	grid[y][x] = grid[y - 1][x] + grid[y][x - 1]
	return grid[y][x]

def main():
	print(calc_paths(20, 20))

utilities.print_runtime(main)