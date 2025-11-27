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


'''
Basically I tried to add difficult parameter and 
connect it to the initializing of the 
SudokuGenerator class while meeting requirements
for Sudoku Generator. Though if you found 
better way that is fine.
'''
