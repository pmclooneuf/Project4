import pygame as pg
from constants import *


class Cell:
    def __init__(self, value, row, col, screen, sketched=0):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched = sketched
        '''
        if self.value == 0:
            self.sketched = 0
        else:
            self.sketched = None
        '''

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self):
        if self.selected:
            self.screen.fill(BG_COLOR)
            pg.draw.rect(self.screen, (250, 0, 0), pg.Rect(67 * self.col, 67 * self.row, 66, 66), 4)
            self.selected = False

        if self.value != 0:
            num_font = pg.font.Font(None, 100)
            num_surf = num_font.render(str(self.value), 1, (0, 0, 0))
            num_rect = num_surf.get_rect(
                center=(self.col * WIDTH // 9 + (WIDTH // 18), self.row * (WIDTH // 9) + (WIDTH // 18) + 5))
            self.screen.blit(num_surf, num_rect)

        if self.sketched is not None and self.sketched != 0:
            num_font = pg.font.Font(None, 30)
            num_surf = num_font.render(str(self.sketched), 1, (100, 100, 100))
            num_rect = num_surf.get_rect(
                center=(self.col * WIDTH // 9 + (WIDTH // 18) - 15, self.row * (WIDTH // 9) + (WIDTH // 18) - 10))
            self.screen.blit(num_surf, num_rect)
