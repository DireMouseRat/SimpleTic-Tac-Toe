# put your code here
user_input = int(input())
input_count = 0
input_sum = 0
while user_input != 55:
    input_count += 1
    input_sum += user_input
    user_input = int(input())
print(input_count)
print(input_sum)
if input_count == 0:
    input_count = 1
print(round(input_sum / input_count))
