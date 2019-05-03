# Solution to https://projecteuler.net/problem=86

import itertools
import math
import utilities

TARGET = 1000000
MAX = 3000

def main():
	solutions = set()
	for i in range(1, MAX):
		a = i**2 - 1
		b = 2 * i
		if a // 2 >= MAX and b // 2 >= MAX:
			break
		for j in range(1, i):
			a = i**2 - j**2
			b = 2 * i * j
			if a // 2 >= MAX and b // 2 >= MAX:
				break
			if math.gcd(i, j) == 1 and (i % 2) + (j % 2) < 2:
				for k in range(1, MAX):
					a = k * (i**2 - j**2)
					b = 2 * k * i * j
					c = k * (i**2 + j**2)
					if a // 2 >= MAX and b // 2 >= MAX:
						break
					for n in range(a // 2, 0, -1):
						m = a - n
						if max(m, n, b) < MAX and min(c**2, (b + m)**2 + n**2, (b + n)**2 + m**2) == c**2:
							solutions.add(tuple(reversed(sorted((n, m, b)))))
						else:
							break
					for n in range(b // 2, 0, -1):
						m = b - n
						if max(m, n, a) < MAX and min(c**2, (a + m)**2 + n**2, (a + n)**2 + m**2) == c**2:
							solutions.add(tuple(reversed(sorted((n, m, a)))))
						else:
							break
	solutions = sorted(solutions)
	return solutions[TARGET][0]

if __name__ == "__main__":
	utilities.print_runtime(main)