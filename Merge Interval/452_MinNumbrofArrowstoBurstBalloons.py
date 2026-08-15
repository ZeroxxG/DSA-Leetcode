
# If we sort the interval by ending
n = len(points)
points.sort(key=lambda x: x[1])
arrows = 1
arrow = points[0][1]

for i in range(1, len(points)):
    start = points[i][0]

    if start > arrow:
        # Current arrow cannot burst this balloon
        arrows += 1
        arrow = points[i][1]

return arrows



# If we sort the interval by starting 
# points.sort()
# arrow = points[0][1]
# arrows = 1

# for i in range(1,n):
#     start = points[i][0]
#     end = points[i][1]

#     if start <= arrow:
#         arrow = min(arrow,end)
#     else:
#         arrows+=1
#         arrow = end

# return arrows
