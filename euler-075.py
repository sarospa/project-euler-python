# Solution to https://projecteuler.net/problem=75

import math
import utilities

MAX = 1500000

def main():
	one_triangle = set()
	many_triangles = set()
	for i in range(1, int(math.sqrt(MAX))):
		for j in range(1, i):
			if i**2 + j**2 > MAX:
				break
			if math.gcd(i, j) == 1 and (i % 2) + (j % 2) < 2:
				for k in range(1, MAX):
					a = k * (i**2 - j**2)
					b = 2 * k * i * j
					c = k * (i**2 + j**2)
					n = a + b + c
					if n > MAX:
						break
					if n in one_triangle:
						one_triangle.remove(n)
						many_triangles.add(n)
					elif n not in one_triangle and n not in many_triangles:
						one_triangle.add(n)
	return len(one_triangle)

if __name__ == "__main__":
	utilities.print_runtime(main)