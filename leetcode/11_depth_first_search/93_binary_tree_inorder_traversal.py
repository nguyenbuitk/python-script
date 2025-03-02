from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
    def inorderTraversal2(self, root):
        return self.inorderTraversal2(root.left) +[root.val] + self.inorderTraversal2[root.right] if root else []
root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)

solution = Solution()
print(solution.inorderTraversal(root))