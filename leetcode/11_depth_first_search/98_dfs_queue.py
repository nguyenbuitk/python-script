from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isValidBST(root: Optional[TreeNode]) -> bool:
    minVal, maxVal = float('-inf'), float('inf')
    queue = deque([(root, minVal, maxVal)])
    while queue:
        node, minVal, maxVal = queue.popleft()
        print(f"Current node: {node.val}, minVal: {minVal}, maxVal: {maxVal}")
        if not (minVal < node.val < maxVal):
            return False
        if node.left:
            queue.append((node.left, minVal, node.val))
        if node.right:
            queue.append((node.right, node.val, maxVal))

    return True

root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)
root.right.right = TreeNode(56)
print(isValidBST(root))