class Game:
    def __init__(self):
        self.x, self.o = 'X', 'O'
        self.current_player = self.x
        self.winner = str()
        self.grid_size = 3
        self.top_bottom_borders = '-' * (2 * self.grid_size + 3)
        self.grid = [[' ' for _ in range(0, self.grid_size)] for _ in range(0, self.grid_size)]
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
        print(self.top_bottom_borders)
        for i in range(0, self.grid_size):
            print("| " + ' '.join([p for p in self.grid[i]]) + " |")
        print(self.top_bottom_borders)

    def player_wins(self, p):
        return any([self.horizontal(p), self.vertical(p), self.diagonal(p)])

    def horizontal(self, p):
        return any([all([cell == p for cell in row]) for row in self.grid])

    def vertical(self, p):
        return any([all([self.grid[j][i] == p for j in range(0, self.grid_size)]) for i in range(0, self.grid_size)])

    def diagonal(self, p):
        left_to_right = all([self.grid[i][i] == p for i in range(0, self.grid_size)])
        right_to_left = all([self.grid[i][self.grid_size - i - 1] == p for i in range(0, self.grid_size)])
        return any([left_to_right, right_to_left])

    def empty_spaces(self):
        return any([any(cell == ' ' for cell in row) for row in self.grid])

    def take_turn(self):
        valid = False
        while not valid:
            cell = input("Enter the coordinates: ").replace(' ', '')
            if cell.isnumeric():
                try:
                    a, b = int(cell[0]), int(cell[1])
                except IndexError:
                    continue
                if self.out_of_range(a, b):
                    print("Coordinates should be from 1 to 3!")
                elif self.occupied_cell(a, b):
                    print("This cell is occupied! Choose another one!")
                else:
                    self.apply_cell(a, b)
                    valid = True
            else:
                print("You should enter numbers!")

    def occupied_cell(self, a, b):
        return self.grid[a - 1][b - 1] != ' '

    def out_of_range(self, a, b):
        return any([a < 1, a > self.grid_size, b < 1, b > self.grid_size])

    def apply_cell(self, a, b):
        self.grid[a - 1][b - 1] = self.current_player

    def next_turn(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def declare_winner(self):
        self.print_game_grid()
        print(self.winner)


Game()
