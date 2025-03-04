from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePathDFS(self, root: Optional[TreeNode]) -> List[str]:
    stack = [(root, "")]
    res = []
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            res.append(f"{path}{node.val}")
        if node.left:
            stack.append((node.left, f"{path}{node.val}->"))
        if node.right:
            stack.append((node.right, f"{path}{node.val}->"))
    return res
            

root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)
print(binaryTreePathDFS(root))
