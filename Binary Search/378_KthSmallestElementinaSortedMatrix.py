def func(mid, n, m):
    row = 0   # Top right element of metrix
    cols = m - 1
    count = 0
    while(row<n and cols>=0):
        if matrix[row][cols] <= mid:
            count += cols + 1
            row += 1
        else:
            cols -= 1
    return count


n = len(matrix)
m = len(matrix[0])
low = matrix[0][0]
high = matrix[n-1][m-1]
res = -1

while(low<=high):
    mid = (low+high)//2

    if func(mid,n,m) < k:
        low = mid + 1
    else:
        res = mid
        high = mid - 1
return res

# Brute
# Adding each element into an array
# arr = []
# for row in matrix: 
#     for num in row:
#         arr.append(num)
# arr.sort()

# return arr[k-1]   # k-1 due to indexing 