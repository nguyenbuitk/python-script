from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def sumOfLeftLeaves(root):
    def dfs(node, isLeft):
        if not node:
            return 0
        if isLeft and not node.left and not node.right:
            return node.val
        return dfs(node.left, True) + dfs(node.right, False)
    return dfs(root, False)

root = TreeNode(3)
root.left = TreeNode(4)
print(sumOfLeftLeaves(root))