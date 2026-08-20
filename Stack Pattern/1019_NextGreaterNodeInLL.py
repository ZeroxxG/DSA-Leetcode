prev = None
curr = head
count=0

while(curr):
    count+=1
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
head = prev

stack = []
res = [0] * count
curr = head

for i in range(count-1,-1,-1):
    while(stack and stack[-1]<=curr.val):
        stack.pop()

    if stack:
        res[i] = stack[-1]

    stack.append(curr.val)
    curr = curr.next
return res

# 2nd Approach 
# Turn the list into an array(by looping through list and store elemnt into an new array)
# Then just run the Next Greater Approach