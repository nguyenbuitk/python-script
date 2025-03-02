from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePath(root: Optional[TreeNode]) -> List[str]:
    res = []
    queue = deque([(root, f"{root.val}")])
    print(queue)
    while queue:
        root, str = queue.pop()
        if not root.left and not root.right:
            res.append(str)
        if root.left:
            queue.append((root.left, f"{str}->{root.left.val}"))
        if root.right:
            queue.append((root.right, f"{str}->{root.right.val}"))
    return res