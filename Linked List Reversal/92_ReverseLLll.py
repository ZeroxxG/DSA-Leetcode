if left == right:
    return head

prev = None
curr = head
count = 1

while count < left: # Traverse till left
    prev = curr
    curr = curr.next
    count += 1

first = prev   
reverse_start = curr    # first element of range to traverse

while count <= right:   # Traverse til right
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
    count += 1

if first:
    first.next = prev
else:
    head = prev

reverse_start.next = curr

return head