from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def sumOfLeftLeaves(root):
    def dfs(node, parent):
        if not node:
            return 0
        if not node.left and not node.right and parent and parent.left == node:
            return node.val
        return dfs(node.left, node) + dfs(node.right, node)
    return dfs(root, None)

root = TreeNode(3)
root.left = TreeNode(4)
print(sumOfLeftLeaves(root))