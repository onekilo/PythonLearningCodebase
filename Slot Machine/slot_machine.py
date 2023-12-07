import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


class SlotMachine:
    def __init__(self):
        self.account_balance = 0

    def play(self):
        start_index = 0

        while True:
            if start_index == 0:
                self.make_deposit()
                print()
                start_index += 1

            if start_index > 0:
                print(f"Your balance is ${self.account_balance}")
            prompt = input("Press enter to play, q to quit: ")
            if prompt.lower() == "q":
                break

            lines = self.get_lines()
            bet_amount = self.bet()
            # check if there is enough balance to cover the bet
            if self.account_balance < lines * bet_amount:
                print(
                    'You don"t have enough balance in your account to cover the bet\n'
                )
                prompt = input(
                    f"Your balance is {self.account_balance}, would you like to make a deposit? (Y=yes, N=no)"
                )
                if prompt.lower() == "y":
                    self.make_deposit()
                    continue
                else: 
                    continue
            self.account_balance -= bet_amount * lines
            self.spin(symbol_count, symbol_value)
            print(f"Your have placed a bet on {lines} lines at ${bet_amount}/line")
            spin_outcome = self.spin(symbol_count, symbol_value)
            lines_won, amount_won = self.check_winnings(spin_outcome, lines, bet_amount)

            self.print_game(spin_outcome)

            if lines_won > 0:
                print(f"You have won on {lines_won} lines for a total of ${amount_won}")
            else:
                print("Better luck next time\n")
       

    def print_game(self, spin_outcome):
        for r in range(len(spin_outcome)):
            print("| ", end="")
            print(" | ".join(spin_outcome[r]), end="")
            print(" |")


    def check_winnings(self, spin_outcome, lines, bet_amount):
        
        lines_won = 0
        amount_won = 0
        for line in range(ROWS):
           
            if all(x == spin_outcome[line][0] for x in spin_outcome[line]):
                # winning_lines.append(row)
                if lines_won < lines:
                    lines_won += 1
                    amount_won += (
                        symbol_value[spin_outcome[line][0]] * ROWS
                    ) * bet_amount
        self.account_balance += amount_won
        return lines_won, amount_won

    def spin(self, symbol_count, symbol_value):
        # make a list of symbols
        symbol_lst = []
        for symbol, val in symbol_count.items():
            for _ in range(val):
                symbol_lst.append(symbol)

        # choose randomly from the symbol_lst. column wise
        random_col_choices = []

        for _ in range(COLS):
            symbol_lst_copy = symbol_lst[:]
            temp_list = []
            for _ in range(ROWS):
                choice = random.choice(symbol_lst_copy)
                temp_list.append(choice)
                symbol_lst_copy.remove(choice)
            random_col_choices.append(temp_list)

        # make a transverse of the random_col_choices to make a proper representation of the game
        spin_lst = []
        for r in range(ROWS):
            temp_list = []
            index = 0
            while index < ROWS:
                temp_list.append(random_col_choices[index][r])
                index += 1
            spin_lst.append(temp_list)

        return spin_lst

    def bet(self):
        while True:
            try:
                bet_amount = int(
                    input(f"How much would you like to bet per line? (1-{MAX_BET})")
                )
                if MAX_BET < bet_amount or bet_amount < 1:
                    raise ValueError

                break
            except ValueError:
                print("Enter a valid amount")
        return bet_amount

    def get_lines(self):
        while True:
            try:
                lines = int(
                    input(
                        f"How many lines would you like to bet on? (choose 1-{MAX_LINES})"
                    )
                )
                if MAX_LINES < lines or lines < 1:
                    raise ValueError
                break
            except ValueError:
                print("Wrong value.")

        return lines

    def make_deposit(self):
        while True:
            try:
                deposit = int(input("How much would you like to deposit? "))
                if deposit < 1:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid amount ")
                continue

        self.account_balance += deposit
        return deposit


game = SlotMachine()

if __name__ == '__main__':
    game.play()
