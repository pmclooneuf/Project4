import math, random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for col in range(9)] for row in range(9)]
        self.box_length = int(math.sqrt(self.row_length)) # important that it's int lol

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):  # row 0, 1, 2...
        if num in self.board[row]:
            return False
        else: # technically not needed i guess 
            return True

    def valid_in_col(self, col, num):
        # get the column as a list
        column = [row[col] for row in self.board]
        # now check in that column list
        if num in column:
            return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num): # can pass in any row and col start, gets box bounds from there
        # get box boundaries
        row_start = row_start - (row_start % 3)
        col_start = col_start - (col_start % 3)
        # get the box as a list
        box = []
        for row in self.board[row_start:row_start + 3]:
            box.extend(row[col_start:col_start + 3])
        # now check in that box list
        if num in box:
            return False
        else:
            return True

    def is_valid(self, row, col, num): # just checks using the other 3 functions
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start): # plucks number from hat basically, no replacement
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                random_num = random.choice(nums)
                self.board[row][col] = random_num
                nums.remove(random_num)

    def fill_diagonal(self): # fills box at 0,0  3,3  6,6 
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col): # important that the other modulo box boundary thing worked
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
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
        attempts = 0
        while attempts < self.removed_cells:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if self.board[x][y] != 0:
                self.board[x][y] = 0
                attempts += 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()

    board = sudoku.get_board()

    return board
