n = len(nums)
        
leftSum = [0] * n
leftSum[0] = 0

rightSum = [0] * n
rightSum[n-1] = 0

ans = [0] * n

for i in range(1,n):
    leftSum[i] = leftSum[i-1] + nums[i-1]

j = n - 2
while(j>=0):
    rightSum[j] = rightSum[j+1] + nums[j+1]
    j-=1

for i in range(n):
    ans[i] = abs(leftSum[i] - rightSum[i])

return ans