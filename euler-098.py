# Solution to https://projecteuler.net/problem=98

import itertools
import math
import utilities

def anagram_pair_value(word_1, word_2):
	if len(word_1) != len(word_2):
		return 0
	if sorted(word_1) != sorted(word_2):
		return 0
	letters = sorted(set(word_1) | set(word_2))
	number_combos = itertools.permutations(range(10), len(letters))
	best_square = 0
	for combo in number_combos:
		num_1 = word_1
		num_2 = word_2
		for i in range(len(letters)):
			num_1 = num_1.replace(letters[i], str(combo[i]))
			num_2 = num_2.replace(letters[i], str(combo[i]))
		if num_1[0] == "0" or num_2[0] == "0":
			continue
		num_1 = int(num_1)
		num_2 = int(num_2)
		if int(math.sqrt(num_1))**2 == num_1 and int(math.sqrt(num_2))**2 == num_2 and max(num_1, num_2) > best_square:
			best_square = max(num_1, num_2)
	return best_square

def main():
	with open("euler-098-data.txt") as f:
		words = [word[1:len(word)-1] for word in f.read().split(",")]
	best_square = 0
	for word_1 in words:
		for word_2 in words[:words.index(word_1)]:
			square = anagram_pair_value(word_1, word_2)
			if square > best_square:
				best_square = square
	return best_square

if __name__ == "__main__":
	utilities.print_runtime(main)