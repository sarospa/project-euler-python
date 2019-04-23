# Solution to https://projecteuler.net/problem=92

import utilities

def main():
	result_89 = set()
	result_1 = set()
	count = 0
	for i in range(1, 10**7):
		term = i
		while term != 1 and term != 89 and term not in result_89 and term not in result_1:
			term = sum([int(ch)**2 for ch in str(term)])
		if term == 89 or term in result_89:
			count += 1
			result_89.add(i)
		else:
			result_1.add(i)
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)