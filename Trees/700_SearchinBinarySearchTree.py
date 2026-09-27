if not root:
    return root

if root.val == val:
    return root

if val < root.val:
    return self.searchBST(root.left, val)
else:
    return self.searchBST(root.right, val)


# Brute
# if not root:
#     return root   # return none
# if root.val == val:
#     return root

# return self.searchBST(root.left, val) 
# return self.searchBST(root.right, val)