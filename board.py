import pygame as pg
from my_sudoku_generator import generate_sudoku
from constants import *
from my_cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None

        # getting the 2d array with 81 cell objects
        sudoku = generate_sudoku(9, difficulty)
        self.cells = []
        for row in range(len(sudoku)):
            cell_row = []
            for col in range(len(sudoku[0])):
                if sudoku[row][col] != 0:
                    cell_row.append(Cell(sudoku[row][col], row, col, screen, None)) # if immutable, sketched value is none (important!)
                else:
                    cell_row.append(Cell(sudoku[row][col], row, col, screen)) # else just 0 as default
            self.cells.append(cell_row)
            

    def draw(self):

        # self.screen.fill(BG_COLOR)
        # draw borders, maybe change sum stuff lol
        pg.draw.line(self.screen, LINE_COLOR, (0, 0), (WIDTH, 0), BORDER_LINE_THICKNESS) # top
        pg.draw.line(self.screen, LINE_COLOR, (0, 0), (0, self.height), BORDER_LINE_THICKNESS) # left
        pg.draw.line(self.screen, LINE_COLOR, (0, WIDTH), (WIDTH, self.height), BORDER_LINE_THICKNESS) # right
        pg.draw.line(self.screen, LINE_COLOR, (0, self.height), (WIDTH, self.height)) # down

        gap = self.width / 9

        # draw the vertical lines
        for x in range(9):
            if x % 3 == 0: # box lines
                pg.draw.line(self.screen, pg.Color('black'), (x * gap, 0), (x * gap, self.height), BOX_LINE_THICKNESS) # thick
            else: # normal lines
                pg.draw.line(self.screen, pg.Color('black'), (x * gap, 0), (x * gap, self.height), LINE_THICKNESS) # thin

        # draw the horizontal lines
        for x in range(9):
            if x % 3 == 0:
                pg.draw.line(self.screen, pg.Color('black'), (0, x * gap), (self.width, x * gap), BOX_LINE_THICKNESS)
            else:
                pg.draw.line(self.screen, pg.Color('black'), (0, x * gap), (self.width, x * gap), LINE_THICKNESS)

        # draw cells
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                self.cells[row][col].draw() 
                    # num_surf = num_font.render(str(self.cells[row][col]), 1, (0, 0, 0))
                    # num_rect = num_surf.get_rect(center = (col*WIDTH//9 + (WIDTH//18), row*(WIDTH//9) + (WIDTH//18) + 5))
                    # self.screen.blit(num_surf, num_rect)
    
    def select(self, row, col):
        self.cells[row][col].selected = True
        self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        row, col = y//(self.height//9), x//(WIDTH//9)
        if y < self.height:
            return (row, col) # only when click is in board and not menu below
        else:
            return None

    def clear(self):
        pass
    
    def sketch(self, value): # maybe dont need to use?
        pass
    
    def place_number(self, value):
        self.selected_cell.value = value
        self.selected_cell.sketched = 0

    def reset_to_original(self):
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                if self.cells[x][y].sketched == None:
                    self.cells[x][y].set_cell_value(self.cells[x][y].value)
                else:
                    self.cells[x][y].set_sketched_value(0)
        self.selected = False

    def is_full(self):
        pass

    def update_board():
        pass

    def find_empty():
        pass
    
    def check_board(self):
        pass

    