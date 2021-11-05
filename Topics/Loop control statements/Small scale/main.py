floats = []
done = False
while not done:
    user_input = str(input())
    if user_input == '.':
        done = True
    else:
        floats.append(float(user_input))
print(min(floats))

# In one line...
# print(min(float(x) for x in iter(input, ".")))
