# Solution to https://projecteuler.net/problem=54

import utilities

values = "23456789TJQKA"

def value_to_int(value):
	if value == "T":
		return 10
	elif value == "J":
		return 11
	elif value == "Q":
		return 12
	elif value == "K":
		return 13
	elif value == "A":
		return 14
	else:
		return int(value)

def check_straight(hand, flush):
	if len({card[1] for card in hand}) == 1 or not flush:
		straight_values = [value_to_int(card[0]) for card in hand]
		smallest = min(straight_values)
		if smallest + 1 in straight_values and smallest + 2 in straight_values and smallest + 3 in straight_values and smallest + 4 in straight_values:
			return smallest
	return 0

def check_group(hand, amount):
	hand_values = [card[0] for card in hand]
	value_match = [value_to_int(value) for value in values if hand_values.count(value) == amount]
	if len(value_match) > 0:
		return max(value_match)
	return 0

def check_full_house(hand):
	hand_values = [card[0] for card in hand]
	value_match_1 = [value_to_int(value) for value in values if hand_values.count(value) == 3]
	value_match_2 = [value_to_int(value) for value in values if hand_values.count(value) == 2]
	if len(value_match_1) > 0 and len(value_match_2) > 0:
		full_house_values = [max(value_match_1), max(value_match_2)]
		return max(full_house_values) * 100 + min(full_house_values)
	return 0

def check_flush(hand):
	if len({card[1] for card in hand}) == 1:
		flush_values = sorted([value_to_int(card[0]) for card in hand])
		return flush_values[4] * 10**8 + flush_values[3] * 10**6 + flush_values[2] * 10**4 + flush_values[1] * 10**2 + flush_values[0]
	return 0

def check_two_pair(hand):
	hand_values = [card[0] for card in hand]
	value_match = [value_to_int(value) for value in values if hand_values.count(value) == 2]
	if len(value_match) > 1:
		return max(value_match) * 10**2 + min(value_match)
	return 0

def check_highest(hand):
	hand_values = sorted([value_to_int(card[0]) for card in hand])
	return hand_values[4] * 10**8 + hand_values[3] * 10**6 + hand_values[2] * 10**4 + hand_values[1] * 10**2 + hand_values[0]

def check_game(hand_1, hand_2):
	rank_1 = [check_straight(hand_1, True), check_group(hand_1, 4), check_full_house(hand_1), check_flush(hand_1), check_straight(hand_1, False), check_group(hand_1, 3), check_two_pair(hand_1), check_group(hand_1, 2), check_highest(hand_1)]
	rank_2 = [check_straight(hand_2, True), check_group(hand_2, 4), check_full_house(hand_2), check_flush(hand_2), check_straight(hand_2, False), check_group(hand_2, 3), check_two_pair(hand_2), check_group(hand_2, 2), check_highest(hand_2)]
	for i in range(len(rank_1)):
		if rank_1[i] > rank_2[i]:
			return 1
		elif rank_1[i] < rank_2[i]:
			return 0
	return 0

def main():
	games = []
	with open("euler-054-data.txt") as f:
		for line in f.readlines():
			game = []
			for card in line.split():
				game.append(card)
			games.append(game)
	return sum([check_game(game[:5], game[5:]) for game in games])

if __name__ == "__main__":
	utilities.print_runtime(main)