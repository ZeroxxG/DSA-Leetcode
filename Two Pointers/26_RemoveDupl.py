i = 0
j = i + 1
unique = 1

while(j<len(nums)):
    if(nums[j]==nums[i]):
        j += 1
    else:
        nums[i+1] = nums[j]
        i += 1
        j += 1
        unique += 1
return unique
