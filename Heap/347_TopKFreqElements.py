n = len(nums)
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

min_heap = []
for item in freq:
    heapq.heappush(min_heap, (freq[item], item))

    if (len(min_heap) > k):
        heapq.heappop(min_heap)

res = []
for item in min_heap:
    res.append(item[1])  # item[1] - item (3,1) elmt on index 1 is 1 

return res 