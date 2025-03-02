from collections import deque
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

def isCousinsUsingQueue(root: TreeNode, x, y):
    res = []
    queue = deque([(root, None, 0)])
    while queue:
        if len(res) == 2:
            break
        root, parent, depth = queue.pop()
        if root.val == x or root.val == y:
            res.append([parent, depth])
        if root.left:
            queue.append(root.left, root, depth +1)
        if root.right:
            queue.append(root.right, root, depth + 1)
    
    return res[0][0] != res[1][0] and res[0][1] == res[1][1]

def binaryTreePathDFS(root: TreeNode):
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

# DFS in 2D matrix
# DFS to find all connected 'O' cells
directions = [(1,0), (-1,0), (0,1), (0,-1)]
rows, cols = 4, 4
board = []
def dfs(i, j, k, visitedLand):
    visitedLand[k].add((i,j))   # Mark the cell as visited in the current region
    for dr, dc in directions:
        ni, nj = i+dr, j + dc
        # Ensure within bounds, not visited, and is 'O'
        if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visitedLand[k] and board[ni][nj] == "O":
            dfs(ni, nj, k, visitedLand)     # Recursive DFS call

def dfs_method2(board, i, j):
    if i < 0 or i>= rows or j < 0 or j >= cols or board[i][j] != 'O':
        return
    board[i][j] = '#'
    for dr, dc in [(1,0), (-1,0), (0, -1), (0, 1)]:
        dfs_method2(i+dr, j + dc)
root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)
