class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def getDepth(root, val):
    print("test")
    if root == None:
        return float('inf')
    if root.val == val:
        return 0
    return 1 + min(getDepth(root.left, val) , getDepth(root.right, val))

def getDepth2(root, val):
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
    

root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)

print(isCousins(root, 1,2))

    
    