n = len(nums)
zero = 0
one = 0
h = {}
res = 0

for i in range(n):
    if nums[i] == 0: zero+=1
    else: one+=1

    diff = zero - one
    if diff == 0:
        res = max(res, i+1)
        continue

    if diff in h:
        idx = h[diff]
        length = i - idx
        res = max(res, length)
    else:
        h[diff] = i
return res