n = len(lists)
min_heap = []

for i in range(n):
    if lists[i]:
        heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

# have to write this when not using dummy node
# if not min_heap:
#     return None
# val, i, node = heapq.heappop(min_heap)
# head = node
# curr = node
# if node.next:
#     heapq.heappush(min_heap, (node.next.val, i, node.next))

dummy = ListNode(0)
curr = dummy

while min_heap:
    val, i, node = heapq.heappop(min_heap)

    curr.next = node
    curr = node

    if curr.next:
        heapq.heappush(min_heap, (node.next.val, i, node.next))
# return head
return dummy.next