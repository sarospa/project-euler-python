# Solution to https://projecteuler.net/problem=126

import itertools
import utilities

def cuboid_layer(x, y, z, k):
	return (x * y * 2) + (y * z * 2) + (x * z * 2) + (x * 4 * (k - 1)) + (y * 4 * (k - 1)) + (z * 4 * (k - 1)) + (utilities.triangle(max(0, k - 2)) * 8)

def main():
	counts = [0] * 20000
	for x in itertools.count(1):
		if cuboid_layer(x, 1, 1, 1) >= len(counts):
			break
		for y in itertools.count(x):
			if cuboid_layer(x, y, 1, 1) >= len(counts):
				break
			for z in itertools.count(y):
				if cuboid_layer(x, y, z, 1) >= len(counts):
					break
				for k in itertools.count(1):
					cubes = cuboid_layer(x, y, z, k)
					if cubes >= len(counts):
						break
					else:
						counts[cubes] += 1
	return [i for i, val in enumerate(counts) if val == 1000][0]

if __name__ == "__main__":
	utilities.print_runtime(main)