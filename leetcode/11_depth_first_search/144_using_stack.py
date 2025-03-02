def preorderTraversal3(root):
    res, stack = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            res.append(current.val)
            current = current.left
        current = stack.pop()
        current = current.right
    return res
