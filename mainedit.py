import pygame, sys
from board import *
from constants import *
from sudoku_generator import generate_sudoku

# ALL THIS DOES RIGHT NOW IS LAUNCH THE PROGRAM WITH NUMBERS // NEED TO ADD PUTTING IN NUMBERS AND RESET // FEEL FREE TO CHANGE IF NEEDED

def start_screen(screen, title_text_font):
    screen.fill(BG_COLOR)
    sudoku_text = title_text_font.render('Welcome to Sudoku', True, LINE_COLOR)
    screen.blit(sudoku_text, (WIDTH // 2 - sudoku_text.get_width() // 2, 100))
    select_text = title_text_font.render('Select Game Mode:', True, LINE_COLOR)
    screen.blit(select_text, (WIDTH // 2 - select_text.get_width() // 2, 200))

def game_screen(board, screen):
    screen.fill(BG_COLOR)
    board.draw() # draws the grids

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT)) # passing a tuple (width & height)
    pygame.display.set_caption('Sudoku')
    title_text_font = pygame.font.Font(None, 50)

    # initialize difficulty buttons:
    easy_button = Buttons(WIDTH // 2 - BUTTON_WIDTH // 2, 300, 'Easy', action='Easy')
    medium_button = Buttons(WIDTH // 2 - BUTTON_WIDTH // 2, 400, 'Medium', action='Medium')
    hard_button = Buttons(WIDTH // 2 - BUTTON_WIDTH // 2, 500, 'Hard', action='Hard')

    # initialize reset/restart/exit buttons:
    reset_button = Buttons(50, 639, 'Reset', action='Reset')
    restart_button = Buttons(WIDTH // 2 - BUTTON_WIDTH // 2, 639, 'Restart', action='Restart')
    exit_button = Buttons(430, 639, 'Exit', action='Exit')

    # initialize variables:
    screen_type = 'start'
    board = None
    difficulty = None

    # draw initial start screen
    start_screen(screen, title_text_font)
    easy_button.draw(screen)
    medium_button.draw(screen)
    hard_button.draw(screen)
    pygame.display.update()

    # main loop
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # hard quits the program. prevents an error happening after closing program.

        if screen_type == 'start':
            if mouse_click[0]: 
                if easy_button.is_clicked(mouse_pos):
                    difficulty = "easy"
                    puzzle, solution = generate_sudoku(9, 30)
                    board = Board(9, 9, screen)
                    board.board = [[str(num) for num in row] for row in puzzle]
                    board.update_cells()
                    screen_type = "game"

                elif medium_button.is_clicked(mouse_pos):
                    difficulty = "medium"
                    puzzle, solution = generate_sudoku(9, 40)
                    board = Board(9, 9, screen)
                    board.board = [[str(num) for num in row] for row in puzzle]
                    board.update_cells()
                    screen_type = "game"

                elif hard_button.is_clicked(mouse_pos):
                    difficulty = "hard"
                    puzzle, solution = generate_sudoku(9, 50)
                    board = Board(9, 9, screen)
                    board.board = [[str(num) for num in row] for row in puzzle]
                    board.update_cells()
                    screen_type = "game"

            if screen_type == "start":
                start_screen(screen, title_text_font)
                easy_button.draw(screen)
                medium_button.draw(screen)
                hard_button.draw(screen)

        elif screen_type == 'game':
            # initialize graphical board (not sudoku board-- already done above)
            screen.fill(BG_COLOR)

            # set up & draw game screen:
            game_screen(board, screen)
            reset_button.draw(screen)
            restart_button.draw(screen)
            exit_button.draw(screen)

            # handle clicks on game buttons
            if mouse_click[0]:
                if reset_button.is_clicked(mouse_pos):
                    # reset board values ONLY (not difficulty)
                    board = Board(9, 9, screen)

                elif restart_button.is_clicked(mouse_pos):
                    # return to start screen
                    screen_type = 'start'
                    start_screen(screen, title_text_font)

                elif exit_button.is_clicked(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  # ALWAYS KEEP AT END OF THIS WHILE-LOOP. (it updates display to prevent it from being black)

if __name__ == "__main__":
    main()