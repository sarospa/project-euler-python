# Solution to https://projecteuler.net/problem=107

import utilities

def sever_cycle(matrix, index, path):
	if index in path:
		cycle = path[path.index(index):]
		high_vertex = None
		high_value = 0
		for i in range(len(cycle)):
			if matrix[cycle[i]][cycle[(i + 1) % len(cycle)]] > high_value:
				high_vertex = (cycle[i], cycle[(i + 1) % len(cycle)])
				high_value = matrix[cycle[i]][cycle[(i + 1) % len(cycle)]]
		matrix[high_vertex[0]][high_vertex[1]] = None
		matrix[high_vertex[1]][high_vertex[0]] = None
		return True
	for i in range(len(matrix[index])):
		if matrix[index][i] is not None and (len(path) == 0 or i != path[-1]):
			new_path = path.copy()
			new_path.append(index)
			found = sever_cycle(matrix, i, new_path)
			if found:
				return True
	return False

def main():
	matrix = []
	with open("euler-107-data.txt") as f:
		for line in f.read().split():
			dataline = []
			for num in line.split(","):
				if num == "-":
					dataline.append(None)
				else:
					dataline.append(int(num))
			matrix.append(dataline)
	old_total = sum([sum([val for val in line if val is not None]) for line in matrix]) // 2
	while sever_cycle(matrix, 0, []):
		pass
	new_total = sum([sum([val for val in line if val is not None]) for line in matrix]) // 2
	return old_total - new_total

if __name__ == "__main__":
	utilities.print_runtime(main)