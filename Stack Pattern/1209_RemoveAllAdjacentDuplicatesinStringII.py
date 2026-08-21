stack = []
for ch in s:
    if stack and stack[-1][0] == ch:
        stack[-1] = (ch, stack[-1][1] + 1)

        if stack[-1][1] == k:
            stack.pop()
    else:
        stack.append((ch,1))
        
# Convert the pairs into string: (a,2) -> "aa"
res = ""
for char, count in stack:
    res+=(char * count)
return res