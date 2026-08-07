n = len(nums)
total = sum(nums)

leftSum = 0
for i in range(0,n):
    if i > 0:
        leftSum += nums[i-1]
    rightSum = total - leftSum - nums[i] 

    if leftSum == rightSum: return i

else: return -1

# BRUTE
    # n = len(nums)
    # leftSum = [0] * n
    # rightSum = [0] * n

    # for i in range(1,n):
    #     leftSum[i] = leftSum[i-1] + nums[i-1]
    
    # j = n - 2
    # while j>=0:
    #     rightSum[j] = rightSum[j+1] + nums[j+1]
    #     j-=1
    
    # for i in range(n):
    #     if leftSum[i] == rightSum[i]:
    #         return i
    # return -1 