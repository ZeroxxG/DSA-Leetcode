if not head or not head.next:
    return head

length = 1
curr = head
while(curr and curr.next):
    curr = curr.next
    length+=1

k = k % length       # Mainly for (if k >= length) 
if k == 0: return head

new = head
tail = new         # We can also use the curr(its a tale),nstead of making anothr var
for i in range(1,length):
    if i < length-k:
        new = new.next
    tail = tail.next
    
tail.next = head
head = new.next
new.next = None

return head