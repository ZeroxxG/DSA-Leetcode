def good(self, root, res):

    if not root:
        return 

    if root.val >= res:
        self.count += 1

    res = max(res, root.val)

    self.good(root.left, res)
    self.good(root.right, res)

    return self.count


def goodNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    res = float('-inf')
    self.count = 0

    return self.good(root, res)

    # res = max so far
    # self.res becomes global but Maximum must belong to the current path, not the entire tree.