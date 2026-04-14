nums = [1, 2, 3, 4, 5]

rev_list = []

for i in range(len(nums) - 1, -1, -1):
    rev_list.append(nums[i])

print(rev_list)