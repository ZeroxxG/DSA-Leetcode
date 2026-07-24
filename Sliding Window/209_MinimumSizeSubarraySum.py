n = len(nums)
low = 0
high = 0
res = float('inf')  # +ve infinity(max no.)
sum = 0

while(high<n):
    sum = sum + nums[high]
    while(sum>=target):
        length = high-low+1
        res = min(res,length)
        sum = sum - nums[low]
        low += 1
    high += 1
if res == float('inf'): return 0
else: return res