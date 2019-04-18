# Solution to https://projecteuler.net/problem=45

import utilities

def main():
	tn = 286
	pn = 166
	hn = 144
	t = utilities.triangle(tn)
	p = utilities.pentagon(pn)
	h = utilities.hexagon(hn)
	while t != p or t != h:
		if t == min(t, p, h):
			tn += 1
			t = utilities.triangle(tn)
		elif p == min(t, p, h):
			pn += 1
			p = utilities.pentagon(pn)
		elif h == min(t, p, h):
			hn += 1
			h = utilities.hexagon(hn)
	return t

if __name__ == "__main__":
	utilities.print_runtime(main)