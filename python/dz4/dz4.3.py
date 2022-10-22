nums = [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
new_nums = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        new_nums.append(nums[i])

print(nums)
print(new_nums)