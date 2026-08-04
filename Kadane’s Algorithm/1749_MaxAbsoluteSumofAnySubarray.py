minend = nums[0]
maxend = nums[0]
res = abs(nums[0])

for i in range(1,len(nums)):
    v1 = maxend + nums[i]
    v2 = minend + nums[i]
    v3 = nums[i]
    maxend = max(v1,v3)
    minend = min(v2,v3)

    res = max(res, abs(maxend), abs(minend))
return res