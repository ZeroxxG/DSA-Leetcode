def can_place(n, dist):
    cow = 1
    pos = arr[0]
    
    for i in range(1,n):
        if arr[i] - pos < dist:
            continue
        else:
            cow+=1
        pos = arr[i]
    if cow >= k: return True
    else: return False
    

n = len(arr)
arr.sort()
low = 1     
high = arr[n-1] - arr[0]
res = -1
    
while(low<=high):
    mid = (low+high)//2
        
    if can_place(n, mid):
        res = mid
        low = mid + 1
    else:
        high = mid - 1
return res