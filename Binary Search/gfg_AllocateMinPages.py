def can_allocate(maxPage, n):
    count = 1
    total = 0
    for num in arr:
        if total + num > maxPage:
            count += 1
            total = num
        else:
            total += num
            
    if count <= k: return True
    else: return False

n = len(arr)
if k > n :  return -1

low = max(arr)
high = sum(arr)
res = -1
while(low<=high):
    mid = (low+high)//2
    
    if can_allocate(mid, n):
        res = mid
        high = mid - 1
    else:

        low = mid + 1
        
return res