n = len(nums)
res = [-1] * n
stack = []

# If Traversing from Right to Left (reverse)
for i in range(2*n - 1, -1, -1):
    idx = i % n
    while(stack and stack[-1]<=nums[idx]):
        stack.pop()
    if stack:
        res[idx] = stack[-1]

    stack.append(nums[idx])

return res  

# if Traversing left to right 
# for i in range(2*n):
#     index = i % n
#     while( stack and nums[stack[-1]]<nums[index]):
#         idx = stack.pop()
#         res[idx] = nums[index]

#     stack.append(index)