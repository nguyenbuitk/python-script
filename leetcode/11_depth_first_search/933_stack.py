class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x, y):
    res = []
    stack = [(root, None, 0)]
    while stack:
        if len(res) == 2:
            break
        node, parent, depth = stack.pop()
        if node.val == x or node.val == y:
            res.append((parent, depth))
        if node.left:
            stack.append((node.left, node, depth+1))
        if node.right:
            stack.append((node.right, node, depth+1))
    
    return  res[0][0] != res[1][0] and res[0][1] == res[1][1]