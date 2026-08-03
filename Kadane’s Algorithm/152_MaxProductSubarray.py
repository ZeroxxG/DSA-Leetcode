min_end = nums[0]
max_end = nums[0]
res = nums[0]

for i in range(1, len(nums)):
    x = nums[i]
    y = min_end * nums[i]
    z = max_end * nums[i]

    max_end = max(x, max(y,z))
    min_end = min(x, min(y,z))
    # res = max(res, max(max_end, min_end))
    res = max(res, max_end)
return res