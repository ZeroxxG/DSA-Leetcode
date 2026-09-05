n = len(matrix)
m = len(matrix[0])
low = 0
high = n*m-1

while(low<=high):
    mid = (low+high)//2
    row = mid // m
    cols = mid % m

    if matrix[row][cols] == target:
        return True 
    elif matrix[row][cols] < target:
        low = mid + 1
    else:
        high = mid - 1

return False