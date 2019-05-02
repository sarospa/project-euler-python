# Solution to https://projecteuler.net/problem=83

import math
import utilities

matrix = []
mins = []

def main():
	with open("euler-083-data.txt") as f:
		for line in f.readlines():
			dataline = []
			for num in line.split(","):
				dataline.append(int(num))
			matrix.append(dataline)
			mins.append([math.inf] * len(dataline))
	unvisited = {(x, y) for x in range(len(matrix[0])) for y in range(len(matrix))}
	mins[0][0] = matrix[0][0]
	while len(unvisited) > 0:
		current = min([(mins[coord[1]][coord[0]], coord[0], coord[1]) for coord in unvisited])
		x = current[1]
		y = current[2]
		if (x + 1, y) in unvisited and mins[y][x] + matrix[y][x + 1] < mins[y][x + 1]:
			mins[y][x + 1] = mins[y][x] + matrix[y][x + 1]
		if (x - 1, y) in unvisited and mins[y][x] + matrix[y][x - 1] < mins[y][x - 1]:
			mins[y][x - 1] = mins[y][x] + matrix[y][x - 1]
		if (x, y + 1) in unvisited and mins[y][x] + matrix[y + 1][x] < mins[y + 1][x]:
			mins[y + 1][x] = mins[y][x] + matrix[y + 1][x]
		if (x, y - 1) in unvisited and mins[y][x] + matrix[y - 1][x] < mins[y - 1][x]:
			mins[y - 1][x] = mins[y][x] + matrix[y - 1][x]
		unvisited.remove((x, y))
	return mins[len(mins) - 1][len(mins[0]) - 1]

if __name__ == "__main__":
	utilities.print_runtime(main)