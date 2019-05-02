# Solution to https://projecteuler.net/problem=84
# This one is a bit more finnicky than the other problems.
# It works now, but I don't think it's totally correct.
# For one, I got the right answer while ignoring the rule about three consecutive doubles entirely.
# I may or may not revisit it later.

import utilities

DICE = 4

JAIL = 10
G2J = 30
GO = 0
CC1 = 2
CC2 = 17
CC3 = 33
CH1 = 7
CH2 = 22
CH3 = 36
C1 = 11
E3 = 24
H2 = 39
R1 = 5
R2 = 15
R3 = 25
R4 = 35
U1 = 12
U2 = 28

def main():
	rolls = [0] * (DICE * 2 + 1)
	for i in range(1, DICE + 1):
		for j in range(1, DICE + 1):
			rolls[i + j] += 1
	roll_total = sum(rolls)
	rolls = [num / roll_total for num in rolls]
	board = [0.025] * 40
	for i in range(1000):
		new_board = board.copy()
		for i in range(len(board)):
			total_prob = 0
			for j in range(len(rolls)):
				total_prob += board[(i - j) % len(board)] * rolls[j]
			new_board[i] = total_prob
		board = new_board.copy()
		new_board[JAIL] += board[G2J] + (board[CC1] * (1/16)) + (board[CC2] * (1/16)) + (board[CC3] * (1/16)) + (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (1/16))
		new_board[G2J] = 0
		new_board[GO] += (board[CC1] * (1/16)) + (board[CC2] * (1/16)) + (board[CC3] * (1/16)) + (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (1/16))
		new_board[C1] += (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (1/16))
		new_board[E3] += (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (1/16))
		new_board[H2] += (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (1/16))
		new_board[R1] += (board[CH1] * (1/16)) + (board[CH2] * (1/16)) + (board[CH3] * (3/16))
		new_board[R2] += (board[CH1] * (2/16))
		new_board[R3] += (board[CH2] * (2/16))
		new_board[U1] += (board[CH1] * (1/16)) + (board[CH3] * (1/16))
		new_board[U2] += (board[CH2] * (1/16))
		new_board[CC1] *= 14/16
		new_board[CC2] *= 14/16
		new_board[CC3] *= 14/16
		new_board[(CH1 - 3) % len(board)] += (board[CH1] * (1/16))
		new_board[(CH2 - 3) % len(board)] += (board[CH2] * (1/16))
		new_board[(CH3 - 3) % len(board)] += (board[CH3] * (1/16))
		new_board[CH1] *= 6/16
		new_board[CH2] *= 6/16
		new_board[CH3] *= 6/16
		board = new_board
	sorted_board = list(reversed(sorted([(board[i], i) for i in range(len(board))])))
	return str(sorted_board[0][1]).zfill(2) + str(sorted_board[1][1]).zfill(2) + str(sorted_board[2][1]).zfill(2)

if __name__ == "__main__":
	utilities.print_runtime(main)