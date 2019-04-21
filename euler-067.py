# Solution to https://projecteuler.net/problem=67

import utilities

triangle = []

def main():
	triangle = utilities.read_to_2d_list("euler-067-data.txt")
	for i in range(1, len(triangle)):
		for j in range(len(triangle[i])):
			max_val = 0
			if j != 0:
				max_val = triangle[i - 1][j - 1]
			if j != len(triangle[i]) - 1 and triangle[i - 1][j] > max_val:
				max_val = triangle[i - 1][j]
			triangle[i][j] += max_val
	return max(triangle[len(triangle) - 1])

if __name__ == "__main__":
	utilities.print_runtime(main)