from .part1 import read_puzzle_input


def examine(grid, rows, columns, x_point, y_point):

    numbers = set()

    def read_number(x, y):
        number = ''

        # Search left and right sides to complete the number

        left = y
        while left >= 0 and grid[x][left].isdigit():
            number = grid[x][left] + number
            left -= 1

        right = y + 1
        while right < columns and grid[x][right].isdigit():
            number += grid[x][right]
            right += 1

        return number

    # Check all adjacent cells (examine each of the 8 surrounding)
    # -1 (moving left), 0 (staying), 1 (moving right)
    for x_moving in [-1, 0, 1]:
        for y_moving in [-1, 0, 1]:
            x_new, y_new = x_point + x_moving, y_point + y_moving

            # Ensure the new position is within the grid bounds
            if 0 <= x_new < rows and 0 <= y_new < columns:
                if grid[x_new][y_new].isdigit():
                    adjacent_number = read_number(x_new, y_new)
                    if adjacent_number:
                        numbers.add(int(adjacent_number))

    return numbers


def sum_of_gear_ratios():
    grid = read_puzzle_input()

    total_sum = 0
    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):

            character = grid[row][column]
            if character == '*':
                numbers = examine(grid, rows, columns, row, column)
                if len(numbers) == 2:
                    total_sum += (numbers.pop() * numbers.pop())

    return total_sum
