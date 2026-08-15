start.sort()
end.sort()

n = len(start)

res = 0
room = 0
i = 0
j = 0

while(i<n and j<n):
    if start[i] < end[j]:
        room+=1
        i+=1
        res = max(res, room)
    else:
        room-=1
        j+=1

return res