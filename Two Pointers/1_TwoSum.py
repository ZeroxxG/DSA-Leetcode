def two_sum(nums, target):

# hash_map = {}
# for i in range(0,len(nums)):
#     num = nums[i]
#     diff = target - num

#     if diff in hash_map:
#         return [hash_map[diff], i]

#     hash_map[num] = i

    nums.sort()
    n = len(nums)
    i = 0
    j = n - 1
    while i < j:
        sums = nums[i] + nums[j]
        if sums == target: return i, j
        elif sums > target: j -= 1
        else: i += 1

# Function call
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))