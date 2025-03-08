from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode):
    if not root:
        return 
    res = []
    queue = deque([root])
    while queue:
        level_size =  len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(node.val)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
root.right = TreeNode(3)
rightSideView(root)