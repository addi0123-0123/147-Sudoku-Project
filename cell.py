import pygame, sys
from constants import *

class Cell:
    def __init__(self, value, row, col):
        self.value = value # numbers 1-9 or '0'
        self.row = row
        self.col = col

    def set_cell_value(self, value):
        # need to write logic for this.
        pass

    def set_sketched_value(self, value):
        # need to write logic for this.
        pass

    def draw(self, screen):
        num_font = pygame.font.Font(None, NUM_FONT)

        if self.value == '0': # leave cells w/ value '0' empty on screen.
            return

        text_surf = num_font.render(str(self.value), True, PRINTED_NUM_COLOR)
        text_rect = text_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE / 2,
                                               self.row * SQUARE_SIZE + SQUARE_SIZE / 2))
        screen.blit(text_surf, text_rect)
