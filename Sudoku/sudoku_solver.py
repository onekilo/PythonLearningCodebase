class Board:
    def __init__(self):
        self.puzzle = self.process_user_input()

    def process_user_input(self):
        is_safe = False
        while not is_safe:
            user_input = input(
                'Enter sudoku values.\n 0 for blanks and rows separated by "-"\n'
            )
            # remove '-' from user input
            user_input = user_input.replace("-", " ")
            # remove all the spaces from the user input and split the chunks into list format
            user_input = user_input.split()
            # check if the rows conform to sudoku(i.e 9), and that each row has 9 values
            if not self.is_user_input_valid(user_input):
                continue

            puzzle = []
            puzzle_row = []
            for i in range(9):
                puzzle.append(self.get_puzzle_row(user_input, i))
            # print(puzzle)
            is_safe = True

        return puzzle

    def is_user_input_valid(self, user_input):
        # check if there are 9 rows
        if len(user_input) != 9:
            print("Check that you have entered all the rows")
            return False
        # check if there are 9 columns
        for row in user_input:
            if len(row) != 9:
                print(f"Check that you have the correct values in row {row}")
                return False
        return True

    def get_puzzle_row(self, user_input, row_index):
        puzzle_row_str = []
        for row in user_input[row_index]:
            puzzle_row_str.append(row)
        # convert the string characters into int and convert zeros to -1 (for easy readability)
        puzzle_row_digits = []
        for num in puzzle_row_str:
            if num != "0":
                puzzle_row_digits.append(int(num))
            else:
                puzzle_row_digits.append(-1)
        return puzzle_row_digits


# print(board.board)


class Sudoku:
    def __init__(self, board) -> None:
        self.puzzle = board
        self.solve_puzzle(board)

    def solve_puzzle(self, board):
        # get empty cell
        row, col = self.get_next_empty(board)

        # if there are no empty cells: means that the puzzle is solved
        if row == None:
            return True
        # for an empty cell we guess every digit recurcively until we find the right one

        for guess in range(1, 10):
            if self.is_guess_valid(puzzle, guess, row, col):
                puzzle[row][col] = guess
                # check if the puzzle is solved
                if self.solve_puzzle(puzzle):
                    return True
            # reset the cell if the guess is invalid
            puzzle[row][col] = -1
        # if we get here means the solution is not correct
        return False

    def is_guess_valid(self, puzzle, guess, row, col):
        # check if the guessed number is in the row
        if guess in puzzle[row]:
            return False

        # check if the guessed number is in column
        for r in range(9):
            if guess == puzzle[r][col]:
                return False

        # check if the guessed number is in the 3x3 cell
        row_val = (row // 3) * 3
        col_val = (col // 3) * 3
        for r in range(max(0, row_val), min(9, row_val + 3)):
            for c in range(max(0, col_val), min(9, col_val + 3)):
                if puzzle[r][c] == guess:
                    return False

        return True

    def get_next_empty(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == -1:
                    return r, c
        # If there are no empty cells
        return None, None


if __name__ == "__main__":
    puzzle = Board().puzzle
    game = Sudoku(puzzle)
    
        
    print(game.puzzle)
