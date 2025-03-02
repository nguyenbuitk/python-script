from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Traversal using DFS
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(root: TreeNode):
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res

# Inorder traversal using Stack
def inorderTraversal2(root):
    return inorderTraversal2(root.left) +[root.val] + inorderTraversal2[root.right] if root else []

# Get depth of node
def getDepth(root, val):
    def dfs(node, depth):
        if not node: 
            return None
        
        if node.val == val:
            return depth
        
        left_result = dfs(node.left, depth + 1)
        if left_result is not None:
            return left_result
        
        return dfs(node.right, depth + 1)
    return dfs(root,0)
    
# Check is cousins
def isCousins(root: TreeNode, x, y):
    res = []
    def dfs(node, parent, depth):
        if not node: 
            return None
        if node.val == x or node.val == y:
            res.append([parent, depth])
        dfs(node.left, node, depth + 1)
        dfs(node.right, node, depth + 1)
    
    dfs(root, None, 0)
    return res[0][0] != res[1][0] and res[0][1] == res[1][1]

