d = [int(c) for c in list(input())]
print([(d[i] + d[i + 1]) / 2 for i in range(0, len(d) - 1)])
