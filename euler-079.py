# Solution to https://projecteuler.net/problem=79

import itertools
import utilities

def build_password(password, keylog, cap):
	if len(password) + len(set(utilities.flatten(keylog))) > cap:
		return ""
	start_chars = {key[0] for key in keylog if len(key) > 0}
	if len(start_chars) == 0:
		return password
	for char in start_chars:
		new_keylog = [key[:1].replace(char, "") + key[1:] for key in keylog if len(key) > 0]
		new_password = password + char
		new_password = build_password(new_password, new_keylog, cap)
		if len(new_password) > 0:
			return new_password
	return ""

def main():
	with open("euler-079-data.txt") as f:
		keylog = f.read().split()
	for i in itertools.count(1):
		password = build_password("", keylog, i)
		if len(password) > 0:
			return password

if __name__ == "__main__":
	utilities.print_runtime(main)