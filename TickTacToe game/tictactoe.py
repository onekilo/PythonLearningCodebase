from random import randint
import time


class InvalidInputError(Exception):
    pass


board_ = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def make_board(board):
    count = 0
    while count < 3:
        print("| ", board[count], " ", end="")
        count += 1
    print("|")
    while count < 6:
        print("| ", board[count], " ", end="")
        count += 1
    print("|")
    while count < 9:
        print("| ", board[count], " ", end="")
        count += 1
    print("|")


def is_board_empty(board):
    for i in board:
        if i != " ":
            return False
    return True


def initialize_board(board):
    if not is_board_empty(board):
        for i in range(len(board)):
            board[i] = " "
    return board


# Check if the cell is empty
def is_cell_empty(cell, board):
    if board[cell] == " ":
        return True

    return False


# Check if the board is full
def is_board_full(board):
    for i in board:
        if i == " ":
            return False
    return True


def player_computer_move(board):
    computer_move = randint(0, (len(board) - 1))
    while not is_cell_empty(computer_move, board):
        computer_move = randint(0, (len(board) - 1))
    print(f"Computer made a move to {computer_move}")

    return computer_move


def human_player_move(board):
    while True:
        try:
            human_move = int(input("Enter your move: "))
            if human_move > 8:
                raise InvalidInputError("Chose a number between 0 and 8")
            while not is_cell_empty(human_move, board):
                human_move = int(input("Enter your move: "))
            break
        except ValueError:
            print("Enter a valid number!")

        except InvalidInputError as e:
            print(e)

    # if human_move < len(board):
    print(f"You made a move to {human_move}")
    return human_move


# Determine if there is a winner
def is_winner(board):
    # check rows
    if not is_board_empty(board_):
        if (
            board[0] == board[1] == board[2] != " "
            or board[3] == board[4] == board[5] != " "
            or board[6] == board[7] == board[8] != " "
        ):
            return True
        # check coulums
        if (
            board[0] == board[3] == board[6] != " "
            or board[1] == board[4] == board[7] != " "
            or board[2] == board[5] == board[8] != " "
        ):
            return True
        # check diagonals
        if (
            board[0] == board[4] == board[8] != " "
            or board[2] == board[4] == board[6] != " "
        ):
            return True
    return False


# Play the game
def play():
    # give the user the visul representation of the board
    computer_letter = "X"
    human_letter = "O"
    make_board(board_)
    print("Use the template above to guide your selection")
    make_board(initialize_board(board_))
    turn = 0
    while not is_winner(board_) and not is_board_full(board_):
        time.sleep(1)
        if turn % 2 == 0:
            board_[player_computer_move(board_)] = computer_letter
        else:
            board_[human_player_move(board_)] = human_letter
        make_board(board_)
        turn += 1

    if is_winner(board_):
        if turn % 2 == 0:  # Human won since turn is always incremented after
            print("You won!!! Congratulations!!!")
        else:
            print("Computer won. Better Luck next time")
    if is_board_full(board_):
        print("It's a tie. Game over!!")

if __name__ == '__main__':
    play()
