def func(capacity, n):
    total = 0
    count = 1
    for w in weights:
        if total + w > capacity:
            count += 1
            total = w
        else:
            total += w
    if count <= days: return True  # means capacity equal ya zyda h
    else: return False      # means capacity kam h

n = len(weights)
low = max(weights)
high = sum(weights)
res = 0

while(low<=high):
    mid = (low+high)//2

    if func(mid, n):
        res = mid
        high = mid - 1
    else:
        low = mid + 1
return res