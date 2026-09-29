# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_small(self, asc):
        if not asc:
            return None
        small = asc.pop()
        right_child = small.right
        while right_child:
            asc.append(right_child)
            right_child = right_child.left
        return small

    def get_big(self, desc):
        if not desc:
            return None
        big = desc.pop()
        left_child = big.left
        while left_child:
            desc.append(left_child)
            left_child = left_child.right
        return big

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        asc = []   # ascending - [2,3,4,5,6,7]
        desc = []   # descending - [7,6,5,4,3,2]

        t = root
        while t:
            asc.append(t)
            t = t.left
        t = root
        while t:
            desc.append(t)
            t = t.right

        i = self.get_small(asc)
        j = self.get_big(desc)

        # Now i, j act as two pointers (Basic two sum)
        while i and j and i.val <= j.val:
            sum = i.val + j.val

            if sum == k:
                return True
            elif sum < k:
                i = self.get_small(asc) # (basically, i += 1)
            else:
                j = self.get_big(desc)  # ( j -= 1)
        
        return False

        # Brute Approach:
        # Traverse the tree inorderly and push the node into an array
            # fun(root.left)
            # arr.append(root.val)
            # fun(root.right)
        # inorder traversal will give sorted array (for BST)
        # Then apply basic 2-Sum on that array