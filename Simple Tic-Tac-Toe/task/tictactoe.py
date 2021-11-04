class Game:
    def __init__(self):
        self.player = 'X'
        self.winner = str()
        self.grid = [[' ' for _ in range(0, 3)] for _ in range(0, 3)]
        self.start_game()

    def print_game_grid(self):
        print("---------")
        print(f"| {self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]} |")
        print(f"| {self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]} |")
        print(f"| {self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]} |")
        print("---------")

    def start_game(self):
        while not self.game_over():
            self.print_game_grid()
            self.take_turn()
            self.next_turn()
        self.declare_winner()

    def game_over(self):
        x, o = 'X', 'O'
        x_wins = self.horizontal(x) or self.vertical(x) or self.diagonal(x)
        o_wins = self.horizontal(o) or self.vertical(o) or self.diagonal(o)
        if x_wins:
            self.winner = 'X wins'
            return True
        elif o_wins:
            self.winner = 'O wins'
            return True
        elif self.empty_spaces():
            return False
        self.winner = 'Draw'
        return True

    def horizontal(self, p):
        return (self.grid[0][0] == p and self.grid[0][1] == p and self.grid[0][2] == p) or \
               (self.grid[1][0] == p and self.grid[1][1] == p and self.grid[1][2] == p) or \
               (self.grid[2][0] == p and self.grid[2][1] == p and self.grid[2][2] == p)

    def vertical(self, p):
        return (self.grid[0][0] == p and self.grid[1][0] == p and self.grid[2][0] == p) or \
               (self.grid[0][1] == p and self.grid[1][1] == p and self.grid[2][1] == p) or \
               (self.grid[0][2] == p and self.grid[1][2] == p and self.grid[2][2] == p)

    def diagonal(self, p):
        return (self.grid[0][0] == p and self.grid[1][1] == p and self.grid[2][2] == p) or \
               (self.grid[0][2] == p and self.grid[1][1] == p and self.grid[2][0] == p)

    def empty_spaces(self):
        pass

    def take_turn(self):
        valid = False
        while not valid:
            cell = input("Enter the coordinates: ")
            if cell[0:3:2].isnumeric():
                a, b = int(cell[0]), int(cell[2])
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
        return a < 1 or a > 3 or b < 1 or b > 3

    def apply_cell(self, a, b):
        self.grid[a - 1][b - 1] = self.player

    def next_turn(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def declare_winner(self):
        self.print_game_grid()
        print(self.winner)


Game()
