n = len(nums)
low = 0
res = 0
count = 0

for high in range(n):
    if nums[high]==0: count+=1

    while(count>k):
        if nums[low]==0: count-=1
        low += 1
        
    length = high - low + 1
    res = max(res,length)

return res