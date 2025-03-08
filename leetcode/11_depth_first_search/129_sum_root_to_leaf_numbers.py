class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: TreeNode):
    res = []
    def dfs(node, sum):
        if not node:
            return
        sum = sum*10 + node.val
        if not node.left and not node.right:
            res.append(sum)
        else:
            dfs(node.left, sum)
            dfs(node.right, sum)
    
    dfs(root, 0)
    return sum(res)
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)

root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sumNumbers(root))
