stack = []
for i in range(0,len(s)):
    if stack and s[i] == stack[-1]:
        stack.pop()
        continue
    stack.append(s[i])

result = "".join(stack)
return result