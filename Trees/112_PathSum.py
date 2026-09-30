total = 0
self.res = False

def sum(root, total):

    if not root:
        return None

    total += root.val

    if not root.left and not root.right:
        if total == targetSum:
            self.res = True
            return

    sum(root.left, total)
    sum(root.right, total)

sum(root, total)
return self.res