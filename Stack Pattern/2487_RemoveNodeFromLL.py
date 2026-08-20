# Reverse the list
prev = None
curr = head
while(curr):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
head = prev

# Find next greater and remove nodes
stack = []
prev = None
curr = head
while curr :
    while(stack and stack[-1]<=curr.val):
        stack.pop()
    if stack:
        prev.next = curr.next
    else:
        prev = curr
        stack.append(curr.val)

    curr = curr.next

# Reverse Back the list
prev = None
curr = head
count = 0
while(curr):
    count+=1
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
head = prev

return head