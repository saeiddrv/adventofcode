from .part1 import read_puzzle_input, find_calibration_value
import re

WORDS_DIGITS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


def replace_words_with_digits(line):
    # Find all numbers (digits or letters) in their occurrence order
    pattern = f"(?=({'|'.join(WORDS_DIGITS.keys())}|{'|'.join(WORDS_DIGITS.values())}))"
    matches = re.finditer(pattern, line)
    result = [match.group(1) for match in matches if match.group(1)]

    # Convert the first and last numbers to digits if they are not!
    if len(result) >= 1 and result[0].isalpha():
        line = line.replace(result[0], WORDS_DIGITS.get(result[0]))
    if len(result) >= 2 and result[-1].isalpha():
        line = line.replace(result[-1], WORDS_DIGITS.get(result[-1]))

    return line


def sum_of_calibration_values():
    lines = read_puzzle_input()

    total_sum = 0

    for line in lines:
        line = replace_words_with_digits(line)
        calibration_value = find_calibration_value(line)
        if calibration_value:
            total_sum += calibration_value

    return total_sum
