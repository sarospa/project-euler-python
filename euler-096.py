# Solution to https://projecteuler.net/problem=96

import copy
import utilities

def get_col(sudoku, col):
	return [row[col] for row in sudoku]

def get_block(sudoku, row, col):
	block_row = row // 3 * 3
	block_col = col // 3 * 3
	return utilities.flatten([row[block_col:block_col+3] for row in sudoku[block_row:block_row+3]])

def solve_sudoku(sudoku, start_row, start_col):
	for i in range(start_row, len(sudoku)):
		for j in range((start_col if i == start_row else 0), len(sudoku[0])):
			if sudoku[i][j] == 0:
				for n in [num for num in range(1, 10) if num not in sudoku[i] and num not in get_col(sudoku, j) and num not in get_block(sudoku, i, j)]:
					sudoku_copy = copy.deepcopy(sudoku)
					sudoku_copy[i][j] = n
					sudoku_copy = solve_sudoku(sudoku_copy, i, j)
					if sudoku_copy is not None:
						return sudoku_copy
				return None
	return sudoku

def main():
	sudokus = []
	with open("euler-096-data.txt") as f:
		sudoku_line = 0
		sudoku = []
		for line in f.readlines():
			if sudoku_line > 0:
				sudoku.append([int(digit) for digit in line[:9]])
			if sudoku_line == 9:
				sudokus.append(sudoku)
				sudoku = []
			sudoku_line = (sudoku_line + 1) % 10
	for sudoku in sudokus:
		pass
	total = 0
	for sudoku in sudokus:
		solved = solve_sudoku(sudoku, 0, 0)
		total += solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)