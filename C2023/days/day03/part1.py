from pkg_resources import resource_filename

PUZZLE_INPUT_FILE = 'day03_input.txt'


def read_puzzle_input():
    with open(resource_filename('resources', PUZZLE_INPUT_FILE), 'r') as file:
        lines = file.readlines()
    lines = [line.strip().lower() for line in lines]
    return lines


def is_symbol(character):
    return character not in '0123456789.'


def is_adjacent_to_symbol(grid, rows, columns, x_point, y_point, number_length):

    def search():
        # Check all adjacent cells (examine each of the 8 surrounding)
        # -1 (moving left), 0 (staying), 1 (moving right)
        for x_moving in [-1, 0, 1]:
            for y_moving in [-1, 0, 1]:
                x_new, y_new = x_point + x_moving, y_point + y_moving

                # Ensure the new position is within the grid bounds
                if 0 <= x_new < rows and 0 <= y_new < columns:
                    if is_symbol(grid[x_new][y_new]):
                        return True

    # Check per number digit's position
    # The first iterate is always from the last digit's position
    for counter in range(number_length):
        if search():
            return True
        else:
            y_point -= 1

    return False


def sum_of_numbers_adjacent_to_symbols():
    grid = read_puzzle_input()

    total_sum = 0
    number = ''  # A place to keep a number
    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):

            if grid[row][column].isdigit():
                # Build the number
                number += grid[row][column]

                # Check if the number continues in the next cell
                if column + 1 < columns and grid[row][column + 1].isdigit():
                    continue

                if is_adjacent_to_symbol(grid, rows, columns, row, column, len(number)):
                    total_sum += int(number)

            else:
                number = ''  # Reset the number

    return total_sum
