class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
def inOrderTravese(root: TreeNode):
    if root == None: 
        return
    inOrderTravese(root.left)
    print(root.val)
    inOrderTravese(root.right)
    
def preOrderTravese(root: TreeNode):
    if root == None: 
        return
    print(root.val)
    preOrderTravese(root.left)
    preOrderTravese(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    preOrderTravese(root)
    solution = Solution()
    print("maxDepth: ", solution.maxDepth(root))