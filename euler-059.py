# Solution to https://projecteuler.net/problem=59

import itertools
import utilities

letters = range(ord('a'), ord('z') + 1)

def decrypt(cipher, password):
	return ''.join([chr(x[0] ^ x[1]) for x in zip(cipher, itertools.cycle(password))])

def find_pass_char(cipher, index):
	best_match = 0
	best_e_match = 1
	for pass_char in letters:
		plaintext = decrypt(cipher[index::3], [pass_char])
		e_freq = len([ch for ch in plaintext if ch == 'e']) / len(plaintext)
		if abs(e_freq - 0.127) < best_e_match:
			best_match = pass_char
			best_e_match = abs(e_freq - 0.127)
	return best_match

def main():
	with open("euler-059-data.txt") as f:
		cipher = [int(num) for num in f.read().split(",")]
	password = []
	for i in range(3):
		password.append(find_pass_char(cipher, i))
	plaintext = decrypt(cipher, password)
	return sum([ord(ch) for ch in plaintext])

if __name__ == "__main__":
	utilities.print_runtime(main)