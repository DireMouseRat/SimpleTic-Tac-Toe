def horizontal(c):
    return (s[0] == c and s[1] == c and s[2] == c) or \
           (s[3] == c and s[4] == c and s[5] == c) or \
           (s[6] == c and s[7] == c and s[8] == c)


def vertical(c):
    return (s[0] == c and s[3] == c and s[6] == c) or \
           (s[1] == c and s[4] == c and s[7] == c) or \
           (s[2] == c and s[5] == c and s[8] == c)


def diagonal(c):
    return (s[0] == c and s[4] == c and s[8] == c) or \
           (s[2] == c and s[4] == c and s[6] == c)


def print_game_grid(grid):
    p = str()
    for i in range(0, 3):
        for j in range(0, 3):
            p += grid[i][j] + ' '
    print(f"""---------
| {p[:6]}|
| {p[6:12]}|
| {p[12:]}|
---------""")


# Get initial string of cell values and replace underscores with spaces
s = input("Enter cells: ").replace('_', ' ')

# Transform input string into a list of lists
cells, k = list(), 0
for i in range(0, 3):
    cells.append(list())
    for j in range(0, 3):
        cells[i].append(s[k])
        k += 1

print_game_grid(cells)

valid = False
a, b = int(), int()
while not valid:
    cell = input("Enter the coordinates: ")
    if cell[0:3:2].isnumeric():
        a = int(cell[0])
        b = int(cell[2])
        if a < 1 or a > 3 or b < 1 or b > 3:
            print("Coordinates should be from 1 to 3!")
        elif cells[a - 1][b - 1] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            cells[a - 1][b - 1] = 'X'
            valid = True
    else:
        print("You should enter numbers!")


print_game_grid(cells)

x, o = 'X', 'O'
x_wins = horizontal(x) or vertical(x) or diagonal(x)
o_wins = horizontal(o) or vertical(o) or diagonal(o)

if (x_wins and o_wins) or \
        s.count(x) - s.count(o) > 1 or \
        s.count(o) - s.count(x) > 1:
    print('Impossible')
elif not x_wins and not o_wins:
    if s.count('_') > 0:
        print('Game not finished')
    else:
        print('Draw')
elif x_wins:
    print('X wins')
else:
    print('O wins')
