# Solution to https://projecteuler.net/problem=68

import itertools
import utilities

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
	n_gons = [[(10, pair[0], pair[1])] for pair in itertools.permutations(nums, 2)]
	n_gons = [n_gon + [(pair[0], n_gon[0][2], pair[1])] for n_gon in n_gons for pair in itertools.permutations([num for num in nums if num not in utilities.flatten(n_gon)], 2) if sum(n_gon[0]) == sum((pair[0], n_gon[0][2], pair[1]))]
	n_gons = [n_gon + [(pair[0], n_gon[1][2], pair[1])] for n_gon in n_gons for pair in itertools.permutations([num for num in nums if num not in utilities.flatten(n_gon)], 2) if sum(n_gon[0]) == sum((pair[0], n_gon[1][2], pair[1]))]
	n_gons = [n_gon + [(pair[0], n_gon[2][2], pair[1])] for n_gon in n_gons for pair in itertools.permutations([num for num in nums if num not in utilities.flatten(n_gon)], 2) if sum(n_gon[0]) == sum((pair[0], n_gon[2][2], pair[1]))]
	n_gons = [n_gon + [(sum(n_gon[0]) - (n_gon[3][2] + n_gon[0][1]), n_gon[3][2], n_gon[0][1])] for n_gon in n_gons if sum(n_gon[0]) - (n_gon[3][2] + n_gon[0][1]) not in utilities.flatten(n_gon) and sum(n_gon[0]) - (n_gon[3][2] + n_gon[0][1]) <= 10 and sum(n_gon[0]) - (n_gon[3][2] + n_gon[0][1]) >= 1]
	n_gons = sorted([n_gon[n_gon.index(min(n_gon)):] + n_gon[:n_gon.index(min(n_gon))] for n_gon in n_gons])
	n_gons = [''.join([''.join([str(n) for n in triplet]) for triplet in n_gon]) for n_gon in n_gons]
	return n_gons[-1]

if __name__ == "__main__":
	utilities.print_runtime(main)