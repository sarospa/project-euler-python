# Solution to https://projecteuler.net/problem=11

import utilities

def main():
	grid = []
	with open("euler-011-data.txt") as f:
		for line in f.readlines():
			gridline = []
			for num in line.split():
				gridline.append(int(num))
			grid.append(gridline)
	n = 0
	for i in range(len(grid)):
		for j in range(len(grid[0]) - 3):
			product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
			if product > n:
				n = product
	for i in range(len(grid) - 3):
		for j in range(len(grid[0])):
			product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
			if product > n:
				n = product
	for i in range(len(grid) - 3):
		for j in range(len(grid) - 3):
			product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
			if product > n:
				n = product
			product = grid[i + 3][j] * grid[i + 2][j + 1] * grid[i + 1][j + 2] * grid[i][j + 3]
			if product > n:
				n = product
	print(n)

utilities.print_runtime(main)