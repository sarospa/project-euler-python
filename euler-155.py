# Solution to https://projecteuler.net/problem=155

from fractions import gcd
import utilities as utils

MAX = 18

def parallel(cap_1, cap_2):
	numerator = (cap_1[0] * cap_2[1]) + (cap_2[0] * cap_1[1])
	denominator = cap_1[1] * cap_2[1]
	common = gcd(numerator, denominator)
	return (numerator // common, denominator // common)

def serial(cap_1, cap_2):
	numerator = cap_1[0] * cap_2[0]
	denominator = (cap_1[0] * cap_2[1]) + (cap_2[0] * cap_1[1])
	common = gcd(numerator, denominator)
	return (numerator // common, denominator // common)

def main():
	values = dict()
	start_val = (60, 1)
	values[1] = {start_val}
	all_values = {start_val}
	for i in range(2, MAX + 1):
		values[i] = set()
		for j in range(1, (i // 2) + 1):
			for cap_1 in values[j]:
				for cap_2 in values[i - j]:
					serial_val = serial(cap_1, cap_2)
					parallel_val = parallel(cap_1, cap_2)
					if serial_val not in all_values:
						all_values.add(serial_val)
						values[i].add(serial_val)
					if parallel_val not in all_values:
						all_values.add(parallel_val)
						values[i].add(parallel_val)
	#print(sorted(all_values))
	return len(all_values)

if __name__ == "__main__":
	utils.print_runtime(main)