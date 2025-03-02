from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePathDFS(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    def dfs(root, previous_str):
        if not root.left and not root.right:
            res.append(f"{previous_str}->{root.val}")
        if root.left: 
            dfs(root.left, f"{previous_str}->{root.val}")
        if root.right:
            dfs(root.right, f"{previous_str}->{root.val}")
    dfs(root,"")
    for i, s in enumerate(res):
        res[i] = s.removeprefix('->')
    return res

def binaryTreePathDFSoptimize(root: TreeNode):
    res = []
    def dfs(node, path):
        if not node:
            return
        path += f"->{node.val}" if path else str(node.val)
        if not node.left and not node.right:
            res.append(f"{path}")
        else:            
            dfs(node.left, f"{path}")
            dfs(node.right, f"{path}")
    dfs(root,"")
    return res

root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)
print(binaryTreePathDFS(root))
