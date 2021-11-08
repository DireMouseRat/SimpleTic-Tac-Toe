hashes = 1
for spaces in range(int(input()) - 1, -1, -1):
    print(' ' * spaces + '#' * hashes)
    hashes += 2
