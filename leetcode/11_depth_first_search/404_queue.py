from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: TreeNode):
    res, queue = 0, deque([(root, False)])
    while queue:
        node, isLeftNode = queue.popleft()
        if isLeftNode and not node.left and not node.right:
            res += node.val
        if node.left:
            queue.append((node.left, True))
        if node.right:
            queue.append((node.right, False))
    return res