# Solution to https://projecteuler.net/problem=61

import itertools
import utilities

def extend_cycles(cycles, values):
	next_cycles = []
	for cycle in cycles:
		for n in values:
			if str(cycle[-1][0])[2:4] == str(n[0])[:2] and n[1] not in [term[1] for term in cycle]:
				next_cycles.append(cycle + [n])
	return next_cycles

def main():
	triangles = [(n, 0) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.triangle, itertools.count(1))) if n > 999 and n % 100 > 10]
	squares = [(n, 1) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.square, itertools.count(1))) if n > 999 and n % 100 > 10]
	pentagons = [(n, 2) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.pentagon, itertools.count(1))) if n > 999 and n % 100 > 10]
	hexagons = [(n, 3) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.hexagon, itertools.count(1))) if n > 999 and n % 100 > 10]
	heptagons = [(n, 4) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.heptagon, itertools.count(1))) if n > 999 and n % 100 > 10]
	octagons = [(n, 5) for n in itertools.takewhile(lambda n: n < 10000, map(utilities.octagon, itertools.count(1))) if n > 999 and n % 100 > 10]
	cycles = []
	values = utilities.flatten([squares, pentagons, hexagons, heptagons, octagons])
	for t in triangles:
		for n in values:
			if str(t[0])[2:4] == str(n[0])[:2]:
				cycles.append([t, n])
	for i in range(4):
		cycles = extend_cycles(cycles, values)
	return sum([term[0] for term in [cycle for cycle in cycles if str(cycle[-1][0])[2:4] == str(cycle[0][0])[:2]][0]])

if __name__ == "__main__":
	utilities.print_runtime(main)