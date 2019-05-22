# Solution to https://projecteuler.net/problem=139

import math
import utilities as utils

MAX = 10**8

def main():
	count = 0
	for i in range(2, int(math.sqrt(MAX))):
		j = (-2 * i + math.sqrt(8 * i**2 + 4)) / 2
		if j != int(j):
			j = (-2 * i + math.sqrt(8 * i**2 - 4)) / 2
		if j != int(j):
			continue
		j = int(j)
		if math.gcd(i, j) == 1 and (i % 2) + (j % 2) < 2:
			a = i**2 - j**2
			b = 2 * i * j
			c = i**2 + j**2
			n = a + b + c
			if n > MAX:
				break
			if c % (abs(a - b)) == 0:
				count += (MAX - 1) // n
	return count

if __name__ == "__main__":
	utils.print_runtime(main)