import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant bombs
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == "*":
                continue
            board[row][col] = "*"
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # check all neighboring cells and return the number of bombs neighboring the cell

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue  # in this case we do nothing
                self.board[r][c] = self.get_neighboring_bombs(r, c)

    def get_neighboring_bombs(self, row, col):
        neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue  # we are in the original cell
                if self.board[r][c] == "*":
                    neighboring_bombs += 1
        return neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        # in the case of self.board[][] = 0 dig recursively
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    # this code gets executed when we call print() on a Board object
    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [
            [None for _ in range(self.dim_size)] for _ in range(self.dim_size)
        ]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        # put this together in a string
        string_rep = ""
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = "   "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep


def play(dim_size, num_bombs):
    # show the user an empty board
    board = Board(dim_size, num_bombs)
    print(board)

    safe = True
    while len(board.dug)< board.dim_size**2 - num_bombs:
        user_move = re.split(',(\\s)*', (input('Where do you want to dig? Format row, col: ')))
        row = int(user_move[0])
        col = int(user_move[-1])
        if row>=board.dim_size or row <0 or col <0 or col >= board.dim_size:
            print('Invalid cell. Try again')
            continue
        safe = board.dig(row, col)
        print(board)
        if not safe:
            break # we dug where there was a bomb

    # display the entire board
    for r in range(board.dim_size):
        for c in range(board.dim_size):
            board.dug.add((r,c))
    print(board)
    if safe:
        print('You won!! Congratulations!!')  
    else:
        print('Kaboom!! Better luck next time.') 
    
if __name__ == '__main__': 
    play(10, 5)



