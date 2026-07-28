low = 0
high = 0
f = {}
res = float('-inf')

for high in range(0,len(s)):
    f[s[high]] = f.get(s[high], 0) + 1
    
    while(len(f) > k):
        f[s[low]] -= 1 
        if f[s[low]] == 0:
            del f[s[low]]
        low+=1
        
    if len(f) == k:
        length = high - low + 1
        res = max(res, length)
if res == float('-inf'): return -1
else: return res