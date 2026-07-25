
low = 0
freq = {}
res = float('-inf')
n = len(s)
for high in range(n):
    freq[s[high]] = freq.get(s[high], 0) + 1
    length = high - low + 1
    max_cnt = max(freq.values())
    diff = length - max_cnt

    while(diff>k):
        freq[s[low]] -= 1
        low += 1
        length = high - low + 1
        max_cnt = max(freq.values())
        diff = length - max_cnt

    res = max(res,length)

return res