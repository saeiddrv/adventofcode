from pkg_resources import resource_filename
import re

PUZZLE_INPUT_FILE = 'day02_input.txt'
GAME_POSSIBILITY = {"red": 12, "green": 13, "blue": 14}


def read_puzzle_input():
    games_data = {}

    with open(resource_filename('resources', PUZZLE_INPUT_FILE), 'r') as file:
        lines = file.readlines()

        for line in lines:
            game, data = line.split(':')
            game_number = int(game.split()[1])
            rounds = data.split(';')

            # Initializing a game
            games_data[game_number] = {"red": 0, "green": 0, "blue": 0}

            # Parsing each round
            for game_round in rounds:
                items = game_round.split(',')
                for item in items:
                    count, color = item.strip().split()
                    count = int(count)
                    # Updating the count if it's higher than the current one
                    if count > games_data[game_number][color]:
                        games_data[game_number][color] = count

    return games_data


def is_game_possible(game):
    for key, value in GAME_POSSIBILITY.items():
        if game.get(key) > value:
            return False
    return True


def sum_of_id_of_games():
    games = read_puzzle_input()

    total_sum = 0

    for game_id, game_rounds_result in games.items():
        if is_game_possible(game_rounds_result):
            total_sum += game_id

    return total_sum
