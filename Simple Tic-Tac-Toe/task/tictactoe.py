import random


class Game:
    def __init__(self):
        random.seed()
        self.x, self.o = 'X', 'O'
        self.current_player = random.choice([self.x, self.o])
        self.winner = str()
        self.size = 3
        self.border_dashes = '-' * (2 * self.size + 3)
        self.grid = [[' ' for _ in range(0, self.size)]
                     for _ in range(0, self.size)]
        self.start_game()

    def start_game(self):
        self.print_starting_text()
        while not self.game_over():
            self.print_game_grid()
            self.take_turn()
            self.next_turn()
        self.declare_winner()

    def print_starting_text(self):
        print("=== Welcome to Tic Tac Toe! ===\n")
        print("Enter a row number and a column number to place your mark")
        print(f"For example, the top right corner is 1 {self.size}")
        print("The first player to make a straight line wins!")
        print(f"{self.current_player} will go first\n")

    def game_over(self):
        if self.player_wins(self.x):
            self.winner = 'X wins'
            return True
        elif self.player_wins(self.o):
            self.winner = 'O wins'
            return True
        elif not self.empty_spaces():
            self.winner = 'Draw'
            return True
        return False

    def take_turn(self):
        next_turn = False
        while not next_turn:
            coordinates = input(f"Place an {self.current_player} at: ")
            try:
                row, column = [int(num) - 1 for num in coordinates.split()]
                if self.occupied_cell(row, column):
                    print("This cell is occupied.")
                else:
                    self.apply_cell(row, column)
                    next_turn = True
            except IndexError:
                print(f"Coordinates must be two numbers between 1 and {self.size}.")
            except ValueError:
                print("No letters or special characters are allowed.")

    def print_game_grid(self):
        # print(f"It is {self.current_player}'s turn")
        print(self.border_dashes)
        for i in range(0, self.size):
            print("| " + ' '.join([p for p in self.grid[i]]) + " |")
        print(self.border_dashes)

    def player_wins(self, p):
        return any([self.horizontal(p), self.vertical(p), self.diagonal(p)])

    def horizontal(self, p):
        return any([all([cell == p for cell in row]) for row in self.grid])

    def vertical(self, p):
        return any([all([self.grid[j][i] == p for j in range(0, self.size)])
                    for i in range(0, self.size)])

    def diagonal(self, p):
        left_to_right = all([self.grid[i][i] == p
                             for i in range(0, self.size)])
        right_to_left = all([self.grid[i][self.size - i - 1] == p
                             for i in range(0, self.size)])
        return any([left_to_right, right_to_left])

    def empty_spaces(self):
        return any([any(cell == ' ' for cell in row) for row in self.grid])

    def occupied_cell(self, row, column):
        return self.grid[row][column] != ' '

    def out_of_range(self, row, column):
        return all([0 <= row < self.size, 0 <= column < self.size])

    def apply_cell(self, row, column):
        self.grid[row][column] = self.current_player

    def next_turn(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def declare_winner(self):
        self.print_game_grid()
        print(self.winner)


Game()
