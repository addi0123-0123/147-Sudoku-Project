import math
class Board:
    def __init__(self, rows, cols, screen, difficulty): # ADD difficulty TO PARAMETERS FOR SUDOKU
        self.rows = rows
        self.cols = cols
        self.screen = screen
        if difficulty == "easy":
            removed_cells = 30
        elif difficulty == "medium":
            removed_cells = 40
        elif difficulty == "hard":
            removed_cells = 50
        self.game = SudokuGenerator(9, removed_cells)
        self.cells = [
            [Cell(self.game.get_board()[i][j], i, j) for j in range(self.cols)]
            for i in range(self.rows)
        ]
# Deletes self.board
# Adds difficulty if statements and uses it to initialize SudokuGenerator
#Gets what used to be self.board[i][j],i,j and puts self.game.get_board()
# If implemented deletes def initialize_board() moves it to meet requirements for SudokuGenerator
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.box_length = int(math.sqrt(self.row_length))
        self.removed_cells = removed_cells
        board_list = []
        for i in range (self.row_length):
            board_list.append([0]* self.row_length)
        self.board = board_list
        
    def get_board(self):
        return self.board
    #agree print_board should be moved to sudoku generator based on format
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()
            
    def valid_in_row(self, row, num):
        return num not in self.board[row]
        
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True
        
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + self.box_length):
            for col in range(col_start, col_start + self.box_length):
                if self.board[r][c] == num:
                    return False
        return True

'''
Basically I tried to add difficult parameter and 
connect it to the initializing of the 
SudokuGenerator class while meeting requirements
for Sudoku Generator. Though if you found 
better way that is fine.
'''

'''
Below is the rest of sudoku_generator, plus another
version of valid_in_box method -Jeff
'''
    # another way of doing valid_in_box:
    # def valid_in_box(self, row_start, col_start, num):
    #     for row in range(3):
    #         for col in range(3):
    #             if self.board[row_start + row][col_start + col] == num:
    #                 return False
    #     return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        for row in range(3):
            for col in range(3):
                while True:
                    num = random.randint(1,9) # picks random number from 1 to 9.
                    if self.valid_in_box(row_start, col_start, num):
                        break
                self.board[row_start + row][col_start + col] = num

    def fill_diagonal(self):
        for i in range(0,9,3):
            self.fill_box(i, i)

    # this method was provided from assignment:
    # def fill_remaining(self, row, col):
    #     if (col >= self.row_length and row < self.row_length - 1):
    #         row += 1
    #         col = 0
    #     if row >= self.row_length and col >= self.row_length:
    #         return True
    #     if row < self.box_length:
    #         if col < self.box_length:
    #             col = self.box_length
    #     elif row < self.row_length - self.box_length:
    #         if col == int(row // self.box_length * self.box_length):
    #             col += self.box_length
    #     else:
    #         if col == self.row_length - self.box_length:
    #             row += 1
    #             col = 0
    #             if row >= self.row_length:
    #                 return True
        
    #     for num in range(1, self.row_length + 1):
    #         if self.is_valid(row, col, num):
    #             self.board[row][col] = num
    #             if self.fill_remaining(row, col + 1):
    #                 return True
    #             self.board[row][col] = 0
    #     return False

    # also provided from assignment:
    # def fill_values(self):
    #     self.fill_diagonal()
    #     self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        cells_to_remove = self.removed_cells

        while cells_to_remove > 0:
            selected_cell = random.randint(0, 80) # chooses a random cell
            row = selected_cell // 9 # obtains a row
            col = selected_cell % 9

            if self.board[row][col] != 0:
                self.board[row][col] = 0

            cells_to_remove -= 1 # decrement to end while loop.
            
# also provided from assignment. code after this is OUTSIDE any classes:
# def generate_sudoku(size, removed):
#     sudoku = SudokuGenerator(size, removed)
#     sudoku.fill_values()
#     board = sudoku.get_board()
#     sudoku.remove_cells()
#     board = sudoku.get_board()
#     sudoku.print_board() # for debugging purposes
#     return board

# test run to see if SudokuGenerator is working correctly:
# if __name__ == '__main__':
#     random.seed()
#     print('im running')
#     size = 9 # always size 9
#     removed = 30 # easy mode
#     sudoku = generate_sudoku(size, removed)
