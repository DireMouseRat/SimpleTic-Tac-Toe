nums = input().split()
search = str(input())
indexes = [str(i) for i in range(len(nums)) if nums[i] == search]
print(' '.join(indexes) if indexes else 'not found')
