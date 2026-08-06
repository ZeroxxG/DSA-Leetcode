bestend = nums[0]
worstend = nums[0]
max_sum = nums[0]
min_sum = nums[0]

total = nums[0]

for i in range(1,len(nums)):
    total+=nums[i]

    v1 = bestend + nums[i]
    v2 = worstend + nums[i]
    v3 = nums[i]
    
    bestend = max(v1, v3)
    worstend = min(v2, v3)

    max_sum = max(max_sum, bestend)
    min_sum = min(min_sum, worstend)
    
if max_sum < 0: return max_sum
# if total == min_count: return res
return max(max_sum, total - min_sum)