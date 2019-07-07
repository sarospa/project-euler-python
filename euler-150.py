# Solution to https://projecteuler.net/problem=150

import utilities as utils

HEIGHT = 1000

def main():
	smallest = 0
	utils.linear_congruential(utils.triangle(HEIGHT))
	triangle = []
	candidates = dict()
	index = 1
	for i in range(1, HEIGHT + 1):
		line = []
		for j in range(i):
			line.append(utils.linear_con_cache[index])
			index += 1
		triangle.append(line)
	for i in range(len(triangle)):
		sums = []
		for j in range(i, len(triangle)):
			sums.append(0)
			for k in range(len(sums)):
				sums[k] += triangle[j][i]
				val = sums[k]
				last_layer = (i - 1, j, k)
				if last_layer in candidates:
					val += candidates[last_layer]
					del candidates[last_layer]
				if val < 0:
					if k + i < j:
						candidates[(i, j, k)] = val
					elif val < smallest:
						smallest = val
	return smallest

if __name__ == "__main__":
	utils.print_runtime(main)