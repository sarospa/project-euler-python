# Solution to https://projecteuler.net/problem=102

import utilities

def find_x_intercept(coord_1, coord_2):
	if utilities.sign(coord_1[1]) == utilities.sign(coord_2[1]):
		return None
	x_diff = coord_2[0] - coord_1[0]
	y_diff = coord_2[1] - coord_1[1]
	return coord_1[0] - (coord_1[1] * (x_diff / y_diff))

def main():
	list = []
	with open("euler-102-data.txt") as f:
		for line in f.readlines():
			dataline = []
			nums = line.split(",")
			dataline.append((int(nums[0]), int(nums[1])))
			dataline.append((int(nums[2]), int(nums[3])))
			dataline.append((int(nums[4]), int(nums[5])))
			list.append(dataline)
	total = 0
	for line in list:
		intercepts = sorted([val for val in [find_x_intercept(line[0], line[1]),  find_x_intercept(line[0], line[2]), find_x_intercept(line[1], line[2])] if val is not None])
		if len(intercepts) > 0 and intercepts[0] < 0 and intercepts[-1] > 0:
			total += 1
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)