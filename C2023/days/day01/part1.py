from pkg_resources import resource_filename
import re

PUZZLE_INPUT_FILE = 'day01p01_input.txt'


def read_puzzle_input():
    with open(resource_filename('C2023.resources', PUZZLE_INPUT_FILE), 'r') as file:
        lines = file.readlines()
    lines = [line.strip().lower() for line in lines]
    return lines


def find_calibration_value(line):
    numbers = re.findall(r'\d', line)
    if numbers:
        if len(numbers) == 1:
            calibration_value = int(f'{numbers[0]}{numbers[0]}')
        else:
            calibration_value = int(f'{numbers[0]}{numbers[-1]}')
        return calibration_value
    else:
        return None


def sum_of_calibration_values():
    lines = read_puzzle_input()

    total_sum = 0

    for line in lines:
        calibration_value = find_calibration_value(line)
        if calibration_value:
            total_sum += calibration_value

    return total_sum
