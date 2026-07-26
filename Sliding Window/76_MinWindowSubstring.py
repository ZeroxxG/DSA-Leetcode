if len(s)<len(t):
    return ""

need = {}
for ch in t:
    need[ch] = need.get(ch, 0) + 1

window = {}
got = 0
low = 0
need_count = len(need)
min_length = float('inf')
res =""
n = len(s)

for high in range(n):
    window[s[high]] = window.get(s[high], 0) + 1
    
    # Checks if this character satisfies requirement
    if s[high] in need and window[s[high]]==need[s[high]]:
        got+=1

    # When all characters matched
    while(need_count == got):
        length = high - low + 1
        if length < min_length:
            min_length = length
            res = s[low:high+1]

        window[s[low]] -= 1
        
        if s[low] in need and window[s[low]] < need[s[low]]:
            got-=1

        low+=1

return res


# GIVES TLE
# n = len(s)
# low = 0
# k = ""
# res = ""
# for high in range(n):
#     k += s[high]
#     while all(k.count(ch) >= t.count(ch) for ch in t):
#         if res == "" or len(k) < len(res):
#             res = k
#         lst = list(k)
#         lst.remove(s[low])
#         k = "".join(lst)
#         low+=1
# return res