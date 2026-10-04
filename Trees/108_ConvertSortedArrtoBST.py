def helper(self, nums, left, right):
    if left > right:
        return None

    mid = (left + right)//2

    root = TreeNode(nums[mid])

    root.left = self.helper(nums, left, mid - 1)
    root.right = self.helper(nums, mid + 1, right)

    return root

def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """
    left = 0
    right = len(nums) - 1

    return self.helper(nums, left, right) 

    # Used mid coz it will split the arr into equal parts(same height) (odd len(arr))
    #or it will divide the arr with 1 elemnt extra in one part(+1height)(even len(arr))

    # mid divide the two array as such it will be same height in both side or +1 height in one side
    # Which satisfies the height-balanced concept 