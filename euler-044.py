# Solution to https://projecteuler.net/problem=44

import utilities

pentagonals = set()
pent_index = 1

def generate_pentagonals(max):
	global pent_index
	p = utilities.pentagon(pent_index)
	while p <= max:
		pentagonals.add(p)
		pent_index += 1
		p = utilities.pentagon(pent_index)

def main():
	n = 1
	while True:
		p2 = utilities.pentagon(n)
		generate_pentagonals(p2 * 2)
		diffs = {p2 - p1 for p1 in pentagonals if p2 - p1 in pentagonals and p2 + p1 in pentagonals}
		if len(diffs) > 0:
			return list(diffs)[0]
		n += 1

if __name__ == "__main__":
	utilities.print_runtime(main)