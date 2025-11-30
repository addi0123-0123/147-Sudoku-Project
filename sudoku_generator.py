import math
import random

# FEEL FREE TO CHANGE

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))

        self.board = []
        for i in range(row_length):
            row = []
            for j in range(row_length):
                row.append(0)
            self.board.append(row)

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for r in range(self.row_length):
            if self.board[r][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + self.box_length):
            for c in range(col_start, col_start + self.box_length):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num))

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)

        idx = 0
        for r in range(self.box_length):
            for c in range(self.box_length):
                self.board[row_start + r][col_start + c] = nums[idx]
                idx += 1

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True

        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == (row // self.box_length) * self.box_length:
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        removed = 0
        while removed < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)

            if self.board[row][col] != 0: 
                self.board[row][col] = 0
                removed += 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    full_solution = [row[:] for row in sudoku.get_board()]
    sudoku.remove_cells()
    puzzle = sudoku.get_board()
    return puzzle, full_solution
