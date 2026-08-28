n = len(nums)
low = 0
high = n - 1

while(low<=high):
    mid = (low+high)//2

    if nums[mid] == target:
        return mid

    if nums[low] <= nums[mid]:  # Left sorted part 
        if target >= nums[low] and target <= nums[mid]:#If target in left part 
        # if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:  #Right sorted part
        if target >= nums[mid] and target <= nums[high]:#If targt in right part
            low = mid + 1
        else:
            high = mid - 1
return -1 