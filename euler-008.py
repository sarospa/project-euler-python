import utilities

def main():
	with open("euler-008-data.txt") as f:
		large_num = f.read()
	n = 0
	for i in range(0, len(large_num) - 13):
		val = 1
		for j in range(i, i + 13):
			val = val * int(large_num[j])
		if val > n:
			n = val
	print(n)

utilities.print_runtime(main)