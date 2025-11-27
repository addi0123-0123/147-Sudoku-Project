import pygame, sys
from board import *
from constants import *

def start_screen(screen, title_text_font):
    # draw start screen:
    screen.fill(BG_COLOR)
    sudoku_text = title_text_font.render('Welcome to Sudoku', True, LINE_COLOR)
    screen.blit(sudoku_text, (WIDTH // 2 - sudoku_text.get_width() // 2, 100))
    title_text = title_text_font.render('Select Game Mode:', True, LINE_COLOR)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))

def game_screen(board, screen):
    screen.fill(BG_COLOR)
    board.draw() # draws the grids

    # manually displayed number: (remove later)
    x = Cell('6', 4, 4)
    x.draw(screen)

    board.print_board()  # debugging purposes

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))  # passing a tuple (width & height)
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

    # set up start screen:
    start_screen(screen, title_text_font)
    easy_button.draw(screen)
    medium_button.draw(screen)
    hard_button.draw(screen)
    pygame.display.update()

    # initialize variables:
    screen_type = 'start screen'
    game_over = False
    difficulty = '' # initialize as 'easy' instead?

    # event loop
    while True:

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # hard quits the program. prevents an error happening after closing program.

            if screen_type == 'start screen': 
                if mouse_click[0]:
                    if easy_button.is_clicked(mouse_pos):
                        difficulty = "easy"
                    elif medium_button.is_clicked(mouse_pos):
                        difficulty = "medium"
                    elif hard_button.is_clicked(mouse_pos):
                        difficulty = "hard"

                if difficulty == "easy":
                    board = Board(9, 9, screen, 'easy') #or some logic like this...
                    # Goal is to set up a board of 9x9 w/ randomized
                    # numbers filled in based on chosen difficulty.
                elif difficulty == 'Medium':
                    board = Board(9, 9, screen, 'medium')
                elif difficulty == 'Hard':
                    board = Board(9, 9, screen, 'hard')

                # then, set up & draw game screen:
                game_screen(board, screen)
                reset_button.draw(screen)
                restart_button.draw(screen)
                exit_button.draw(screen)

                screen_type = 'game screen'

            if screen_type == 'game screen':
                # <logic here>
                pass

        pygame.display.update() # ALWAYS KEEP AT END OF THIS WHILE-LOOP. (it updates display to prevent it from being black)

if __name__ == '__main__':
    main()


