import pygame as pg
import sys
from my_board import Board
from constants import *

def start(screen): # this is just the first screen that shows the options and stuff before the game, also gets difficulty
    # background
    background = pg.image.load("images/background image.jpg").convert()
    screen.blit(background, (0, 0))

    # title
    title_font = pg.font.Font(None, 80)
    title_surface = title_font.render("Welcome to Sudoku", 0, 'black')
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # choice message
    choose_font = pg.font.Font(None, 60)
    choose_surface = choose_font.render("Choose a difficulty: ", 0, 'black')
    choose_rectangle = choose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(choose_surface, choose_rectangle)

    #buttons
    button_font = pg.font.Font(None, 50)
    # easy
    easy_text = button_font.render("Easy", 1, 'black')
    easy_surf = pg.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surf.fill('green')
    easy_surf.blit(easy_text, (10, 10))
    easy_rect = easy_surf.get_rect(center=(150, HEIGHT // 2 + 150))
    screen.blit(easy_surf, easy_rect)
    # medium
    medium_text = button_font.render("Medium", 1, 'black')
    medium_surf = pg.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surf.fill('yellow')
    medium_surf.blit(medium_text, (10, 10))
    medium_rect = medium_surf.get_rect(center=(300, HEIGHT // 2 + 150))
    screen.blit(medium_surf, medium_rect)
    # hard
    hard_text = button_font.render("Hard", 1, 'black')
    hard_surf = pg.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surf.fill('red')
    hard_surf.blit(hard_text, (10, 10))
    hard_rect = hard_surf.get_rect(center=(450, HEIGHT // 2 + 150))
    screen.blit(hard_surf, hard_rect)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    return 30
                elif medium_rect.collidepoint(event.pos):
                    return 40
                elif hard_rect.collidepoint(event.pos):
                    return 50
        
        pg.display.update()



def game_over(screen): # later lol
    pass



def main():
    game_over = False

    pg.init()
    pg.display.set_caption("Sudoku")
    WIDTH = 600
    HEIGHT = 700
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    difficulty = start(screen)

    screen.fill(BG_COLOR)

    board = Board(WIDTH, HEIGHT - 100, screen, difficulty) # gens the actual board based on difficulty
    # printed_board = []
    # for row in range(len(board.cells)):
    #     print_row = []
    #     for col in range(len(board.cells[0])):
    #         print_row.append(board.cells[row][col].value)
    #     printed_board.append(print_row)
    # print(printed_board)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                click = board.click(x, y)
                if click is not None:
                    board.select(click[0], click[1])
            
            if event.type == pg.KEYDOWN and board.selected_cell.sketched != None:
                if event.key == pg.K_RETURN:
                    board.place_number(board.selected_cell.sketched)
                elif event.key == pg.K_1:
                    board.selected_cell.sketched = 1
                elif event.key == pg.K_2:
                    board.selected_cell.sketched = 2
                elif event.key == pg.K_3:
                    board.selected_cell.sketched = 3
                elif event.key == pg.K_4:
                    board.selected_cell.sketched = 4
                elif event.key == pg.K_5:
                    board.selected_cell.sketched = 5
                elif event.key == pg.K_6:
                    board.selected_cell.sketched = 6
                elif event.key == pg.K_7:
                    board.selected_cell.sketched = 7
                elif event.key == pg.K_8:
                    board.selected_cell.sketched = 8
                elif event.key == pg.K_9:
                    board.selected_cell.sketched = 9
                


        board.draw()

        pg.display.update()

if __name__ == '__main__':
    main()

