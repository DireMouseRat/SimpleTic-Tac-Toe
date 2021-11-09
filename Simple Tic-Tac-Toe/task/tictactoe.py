class Game:
    def __init__(self):
        self.x, self.o = 'X', 'O'
        self.current_player = self.x
        self.winner = str()
        self.size = 3
        self.border_dashes = '-' * (2 * self.size + 3)
        self.grid = [[' ' for _ in range(0, self.size)]
                     for _ in range(0, self.size)]
        self.start_game()

    def start_game(self):
        while not self.game_over():
            self.print_game_grid()
            self.take_turn()
            self.next_turn()
        self.declare_winner()

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

    def print_game_grid(self):
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

    def take_turn(self):
        next_turn = False
        while not next_turn:
            coordinates = input("Enter the coordinates: ")
            try:
                row, column = [int(num) - 1 for num in coordinates.split()]
                if self.occupied_cell(row, column):
                    print("This cell is occupied! Choose another one!")
                else:
                    self.apply_cell(row, column)
                    next_turn = True
            except IndexError:
                print("Coordinates should be from 1 to 3!")
            except ValueError:
                print("You should enter numbers!")

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
