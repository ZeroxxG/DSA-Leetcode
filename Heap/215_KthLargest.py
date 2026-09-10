n = len(nums)
min_heap = []

for i in range(k):
    heapq.heappush(min_heap, nums[i])

for i in range(k,n):
    if nums[i] <= min_heap[0]:
        continue
    else:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, nums[i])

return min_heap[0]

# we can also do tht for loop of range(n) just like this:
# for i in range(n):
#     heapq.heappush(min_heap, nums[i])
#     heapq.heappop(min_heap)

# pushing an elmnt then poping the top elmnt(smallest) (top elmnt in minHeap is smallst)