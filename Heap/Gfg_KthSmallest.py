n = len(arr)
max_heap = []

for i in range(k):
    heapq.heappush(max_heap, -arr[i])

for i in range(k,n):
    if arr[i] >= -max_heap[0]:
        continue
    else:
        heapq.heappop(max_heap)
        heapq.heappush(max_heap, -arr[i])   # Heap automatically manages the top element

return -max_heap[0]