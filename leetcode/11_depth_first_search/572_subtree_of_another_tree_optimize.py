class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSametree(self, q: TreeNode, p: TreeNode) -> bool:
        if not q and not p: 
            return True
        if not q or not p or q.val != p.val:
            return False
        return self.isSametree(q.left,p.left) and self.isSametree(q.right,p.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    solution = Solution()
    print(solution.isSubtree(root,subRoot))