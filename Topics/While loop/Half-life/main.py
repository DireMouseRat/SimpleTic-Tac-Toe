current_quantity = int(input())
final_quantity = int(input())
half_lives = 1
while current_quantity / 2 > final_quantity:
    current_quantity /= 2
    half_lives += 1
print(half_lives * 12)
