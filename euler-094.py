# Solution to https://projecteuler.net/problem=94

import math
import utilities

MAX = 1000000000

def has_integral_area(base, side):
	if side * 2 <= base or base % 2 == 1:
		return False
	height_sq = side**2 - (base // 2)**2
	height = int(math.sqrt(height_sq))
	return height**2 == height_sq and (base % 4 == 0 or height % 2 == 0)

def main():
	total = 0
	prev = 1
	ratio = 3
	distance = 0
	while True:
		i = int(prev * ratio) + distance
		if i * 3 > MAX:
			break
		if distance > 0:
			distance *= -1
		else:
			distance *= -1
			distance += 1
		if has_integral_area(i, i + 1) and i * 3 + 2 <= MAX:
			total += i * 3 + 2
			ratio = i / prev
			prev = i
			distance = 0
		if has_integral_area(i, i - 1) and i * 3 - 2 <= MAX:
			total += i * 3 - 2
			ratio = i / prev
			prev = i
			distance = 0
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)