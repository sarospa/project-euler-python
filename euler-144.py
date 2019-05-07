# Solution to https://projecteuler.net/problem=144

import math
import utilities

def reflect_point(coord, reflect_coord, reflect_slope):
	normal_slope = -1 / reflect_slope
	normal_y_intercept = reflect_coord[1] - (reflect_coord[0] * normal_slope)
	reflect_y_intercept = coord[1] - (coord[0] * reflect_slope)
	intersect_x = (reflect_y_intercept - normal_y_intercept) / (normal_slope - reflect_slope)
	intersect_y = reflect_y_intercept + (reflect_slope * intersect_x)
	x = intersect_x - (coord[0] - intersect_x)
	y = intersect_y - (coord[1] - intersect_y)
	return (x, y)

def find_cell_intersect(bounce_coord, help_coord):
	slope = (help_coord[1] - bounce_coord[1]) / (help_coord[0] - bounce_coord[0])
	y_intercept = bounce_coord[1] - (bounce_coord[0] * slope)
	a = (4 + slope**2)
	b = 2 * slope * y_intercept
	c = y_intercept**2 - 100
	pos_x = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
	pos_intersect = (pos_x, y_intercept + (slope * pos_x))
	neg_x = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
	neg_intersect = (neg_x, y_intercept + (slope * neg_x))
	if abs(bounce_coord[0] - pos_intersect[0]) + abs(bounce_coord[1] - pos_intersect[1]) < abs(bounce_coord[0] - neg_intersect[0]) + abs(bounce_coord[1] - neg_intersect[1]):
		return neg_intersect
	else:
		return pos_intersect

def main():
	start_coord = (0, 10.1)
	bounce_coord = (1.4,-9.6)
	count = 0
	while not (bounce_coord[1] > 0 and bounce_coord[0] < 0.01 and bounce_coord[0] > -0.01):
		count += 1
		reflected_coord = reflect_point(start_coord, bounce_coord, (-4 * bounce_coord[0]) / bounce_coord[1])
		next_bounce_coord = find_cell_intersect(bounce_coord, reflected_coord)
		start_coord = bounce_coord
		bounce_coord = next_bounce_coord
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)