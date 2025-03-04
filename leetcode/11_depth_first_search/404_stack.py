from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def sumOfLeftLeaves(root):
    stack = [(root, False)]
    res = 0
    while stack:
        node, isLeftNode = stack.pop()
        if not node.left and not node.right and isLeftNode:
           res += node.val
        if node.left:
            stack.append((node.left, True)) 
        if node.right:
            stack.append((node.right, False))
    return res
root = TreeNode(3)
root.left = TreeNode(4)
print(sumOfLeftLeaves(root))