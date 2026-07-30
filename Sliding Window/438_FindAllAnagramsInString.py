n = len(s)
m = len(p)
res = []

if  n < m : return res

need = {}
for ch in p:
    need[ch] = need.get(ch, 0) + 1

low = 0
high = m - 1
f = {}
for i in range(low,high+1):
    f[s[i]] = f.get(s[i], 0) + 1

while(high<n):
    if f == need:
        res.append(low)
    f[s[low]] -= 1
    if f[s[low]] == 0: del f[s[low]]
    low+=1
    high+=1
    if high < n:
        f[s[high]] = f.get(s[high], 0) + 1
return res