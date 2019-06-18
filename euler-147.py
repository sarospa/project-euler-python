# Solution to https://projecteuler.net/problem=147

import utilities as utils

MAX_LENGTH = 47
MAX_HEIGHT = 43

def full_rect_calc(x, y):
	min_side = min(x, y)
	margin = abs(x - y)
	return max(utils.triangle(min_side - 1) * 4 + (min_side * 2 - 1) * margin, 0)

def half_full_rect_calc(x, y):
	return max(full_rect_calc(x, y) - (x + y - 2), 0)

def half_half_rect_calc(x, y):
	return max(half_full_rect_calc(x, y) - max((x + y - 3), 0), 0)

def main():
	rectangle_groups = [[full_rect_calc(x, y) + half_full_rect_calc(x, y) * 2 + half_half_rect_calc(x, y) for x in range(MAX_LENGTH + 1)] for y in range(MAX_HEIGHT + 1)]
	total = 0
	for y in range(1, MAX_HEIGHT + 1):
		for x in range(1, MAX_LENGTH + 1):
			total += utils.triangle(x) * utils.triangle(y)
			for i in range(min(x, y)):
				total += rectangle_groups[y - i][x - i] * (i + 1)
	return total

if __name__ == "__main__":
	utils.print_runtime(main)