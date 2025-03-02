from typing import Optional, List

def preorderTraversal(self, root) -> List[int]:
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

def preorderTraversal(root):
    res = []
    def dfs(root):
        if not root:
            return
        
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    return res


