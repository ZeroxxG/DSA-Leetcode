n = len(nums)
low = 0
high = n - 1

while(low<high):
    mid = (low+high)//2
    if nums[mid] > nums[high]:
        low = mid + 1
    else:
        high = mid  #mid can be our ans thts y we keeps it inside search space
return nums[low] 