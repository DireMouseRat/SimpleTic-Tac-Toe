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


s = input("Enter cells: ")
p = " ".join(s).replace('_', ' ')
x, o = 'X', 'O'
print(f"""---------
| {p[:6]}|
| {p[6:12]}|
| {p[12:]} |
---------""")

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
