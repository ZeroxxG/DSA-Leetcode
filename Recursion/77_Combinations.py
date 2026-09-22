temp = []
res = []
start = 1

def combinations(start, temp):
    if len(temp) == k:
        res.append(temp[:])
        return

    if start > n:
        return

    temp.append(start)
    combinations(start+1, temp)
    temp.pop()

    combinations(start+1, temp)

combinations(start, temp)
return res

# for num in range(start, n+1):
#         temp.append(num)
#         combinations(num+1)
#         temp.pop()