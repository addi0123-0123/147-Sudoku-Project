import pygame, sys
from constants import *
from cell import Cell

class Board:
    def __init__(self, rows, cols, screen): # ADD difficulty TO PARAMETERS FOR SUDOKU
        self.rows = rows
        self.cols = cols
        self.screen = screen
        self.board = self.initialize_board() # do we need this line?
        self.cells = [
            [Cell(self.board[i][j],i,j) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    @staticmethod
    def initialize_board():  # move to SudokuGenerator?
        return[['0' for i in range(9)] for j in range(9)] # maybe '0' should be '-' instead?

    def print_board(self): # for debugging purposes. move to SudokuGenerator?
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def update_cells(self):
        self.cells = [
            [Cell(self.board[i][j], i, j) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def board_is_full(self):
        for row in self.board:
            for cell in row:
                if cell == "0":
                    return False
        return True

    # below func. is directly from ttt_OOP & can replace find_empty:
    ##################################
    # def is_valid(self, row, col):
    #     if 0 <= row <= 8 and 0 <= col <= 8 and self.board[row][col] == '0':
    #         return True
    #     return False
    def find_empty(self, row, col):
        if 0 <= row <= 8 and 0 <= col <= 8 and self.board[row][col] == '0':
            empty_cell = (col, row)     # col = x-coord., row = y-coord.
            return empty_cell
        return None

    def is_full(self):
        if self.find_empty is None:
            return True
        return False
    # logic might be faulty

    def check_board(self, chip_type):
        # checks for win.
        # refer to 'check_if_winner' func. from ttt_OOP.
        # MUST create our own logic to fit sudoku's scenario.
        pass

    def draw(self):
        # draw THIN LINES:
            # horizontal lines:
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i*SQUARE_SIZE),
                (WIDTH, i*SQUARE_SIZE),
                LINE_WIDTH
            )
            # vert lines:
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )

        #draw THICK lines:
            # horizontal lines at rows 0, 3, 6, 9
        for i in range(0, BOARD_ROWS + 1, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH_THICK
            )
            # vertical lines at cols 0, 3, 6, 9
        for i in range(0, BOARD_COLS + 1, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH_THICK
            )

        # go thru each cell (from __init__) to call the DRAW METHOD:
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)

class Buttons:
    def __init__(self, x, y, text, action = None):
        self.rect = pygame.Rect(x,y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.text = text
        self.action = action

    def draw(self, surface):
        text_font = pygame.font.Font(None, 50)

        pygame.draw.rect(surface, LINE_COLOR, self.rect)
        text_surface = text_font.render(self.text, True, BG_COLOR)
        surface.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)