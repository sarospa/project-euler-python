# Solution to https://projecteuler.net/problem=109

import itertools
import utilities

def main():
	singles = list(range(1, 21)) + [25]
	doubles = list(range(2, 41, 2)) + [50]
	triples = list(range(3, 61, 3))
	all_regions = singles + doubles + triples
	return len([c for c in [pair + (value,) for pair in itertools.combinations_with_replacement(all_regions, 2) for value in doubles] + list(itertools.product(all_regions, doubles)) + [(n,) for n in doubles] if sum(c) < 100])

if __name__ == "__main__":
	utilities.print_runtime(main)