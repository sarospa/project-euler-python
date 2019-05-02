# Solution to https://projecteuler.net/problem=82

import utilities

matrix = []
cache = []

def main():
	with open("euler-081-data.txt") as f:
		for line in f.readlines():
			dataline = []
			for num in line.split(","):
				dataline.append(int(num))
			matrix.append(dataline)
			cache.append([None] * len(dataline))
	for y in range(len(matrix)):
		cache[y][0] = matrix[y][0]
	for x in range(1, len(matrix[0])):
		for y in range(len(matrix)):
			cache[y][x] = cache[y][x - 1] + matrix[y][x]
		for y in range(1, len(matrix)):
			if cache[y - 1][x] + matrix[y][x] < cache[y][x]:
				cache[y][x] = cache[y - 1][x] + matrix[y][x]
		for y in range(len(matrix) - 2, 0, -1):
			if cache[y + 1][x] + matrix[y][x] < cache[y][x]:
				cache[y][x] = cache[y + 1][x] + matrix[y][x]
	return min([row[len(row) - 1] for row in cache])

if __name__ == "__main__":
	utilities.print_runtime(main)