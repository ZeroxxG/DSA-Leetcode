def hours(nums, n, speed): # mid = speed
    h = 0
    for num in nums:
        h = h + (num/speed)  # time = distance/speed
        if num % speed != 0:
            h+=1
    return h

n = len(piles)
low = 1
high = max(piles)

while(low<high):
    mid = (low+high)//2
    hour = hours(piles,n,mid)

    if hour > h:
        low = mid + 1
    else:
        high = mid
return low