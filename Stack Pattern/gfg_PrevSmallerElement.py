
n = len(arr)
res = [0] * n
stack = []

for i in range(n):
    while( stack and stack[-1]>=arr[i]):
        stack.pop()
        
    if not stack:
        res[i] = -1
    else:
        res[i] = stack[-1]
    
    stack.append(arr[i])
    
return res