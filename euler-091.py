# Solution to https://projecteuler.net/problem=91

import fractions
import utilities

MAX = 50

def simplify(coord):
	divisor = abs(fractions.gcd(coord[0], coord[1]))
	return (coord[0] // divisor, coord[1] // divisor)

def is_right_triangle(x_1, y_1, x_2, y_2):
	if (x_1 == x_2 and y_1 == y_2) or (x_1 == 0 and y_1 == 0) or (x_2 == 0 and y_2 == 0):
		return False
	if simplify((x_1, y_1)) == simplify((x_2, y_2)) or utilities.sign(x_1 - x_2) == utilities.sign(y_1 - y_2):
		return False
	if (x_1 == 0 and y_2 == 0) or (x_2 == 0 and y_1 == 0):
		return True
	edge_1 = simplify((x_1, y_1))
	edge_2 = simplify((x_2, y_2))
	edge_3 = simplify((abs(y_1 - y_2), abs(x_1 - x_2)))
	return edge_2 == edge_3 or edge_1 == edge_3

def main():
	return len({tuple(sorted(((x_1, y_1), (x_2, y_2)))) for x_1 in range(MAX + 1) for y_1 in range(MAX + 1) for x_2 in range(MAX + 1) for y_2 in range(MAX + 1) if is_right_triangle(x_1, y_1, x_2, y_2)})

if __name__ == "__main__":
	utilities.print_runtime(main)