n = len(s)
freq = {}
res = 0    #float('-inf')
low = 0

for high in range(n):
    freq[s[high]] = freq.get(s[high], 0) + 1

    length = high - low + 1
    while(length>len(freq)):
        freq[s[low]] -= 1
        if freq[s[low]]==0:
            del freq[s[low]]
        low+=1
        length = high - low + 1

    res = max(res, length)

return res