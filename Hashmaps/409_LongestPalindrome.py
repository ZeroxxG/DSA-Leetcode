freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

count = 0
odd = False
for ch in freq:
    if freq[ch] % 2 == 0:
        count += freq[ch]
    else:
        count += (freq[ch] - 1)
        odd = True
if odd == True: return count + 1
else: return count