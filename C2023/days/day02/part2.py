from .part1 import read_puzzle_input


def calculate_power(game):
    power = 1
    for key, value in game.items():
        power *= value
    return power


def sum_of_power_of_games():
    games = read_puzzle_input()

    total_sum = 0

    for game_id, game_rounds_result in games.items():
        total_sum += calculate_power(game_rounds_result)

    return total_sum
