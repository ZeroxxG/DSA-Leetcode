n = len(nums)
sum = 0
res = 0
f = {}
f[0] = 1

for i in range(0,n):
    sum += nums[i]

    ques = sum - k
    freq = f.get(ques, 0)
    res+=freq
    f[sum] = f.get(sum, 0) + 1
return res