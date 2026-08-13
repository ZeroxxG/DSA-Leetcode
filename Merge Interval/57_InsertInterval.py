n = len(intervals)

# Inserting
res = []
insert = False
for i in range(0,n):
    s = intervals[i][0]
    e = intervals[i][1]
    if insert == False and s > newInterval[0]:
        res.append([newInterval[0], newInterval[1]])
        insert = True
    res.append([s,e])
if insert == False:
    res.append([newInterval[0], newInterval[1]])

# Merging
merged = []
start1 = res[0][0]
end1 = res[0][1]
for i in range(1,n+1):
    start2 = res[i][0]
    end2 = res[i][1]

    if end1 >= start2:
        end1 = max(end1,end2)
        continue
    merged.append([start1,end1])
    start1 = start2
    end1 = end2
merged.append([start1, end1])
return merged


# TC - O(n log n)
# SC - O(n)
# newStart = newInterval[0]
# newEnd = newInterval[1]

# intervals.append([newStart,newEnd])
# intervals.sort()

# start1 = intervals[0][0]
# end1 = intervals[0][1]

# merged = []

# for i in range(1,n+1):
#     start2 = intervals[i][0]
#     end2 = intervals[i][1]

#     if end1 >= start2:
#         end1 = max(end1,end2)
#         continue
#     merged.append([start1,end1])
#     start1 = start2
#     end1 = end2
# merged.append([start1, end1])
# return merged