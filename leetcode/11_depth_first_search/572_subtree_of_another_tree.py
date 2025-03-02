class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraverse(root: TreeNode):
    result = []
    def helper(node: TreeNode):
        if node == None:
            result.append(None)
            return 
        result.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return result

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        tree = preorderTraverse(root)
        subTree = preorderTraverse(subRoot)
        print("tree: ", tree)
        print("subTree: ", subTree)
        for idx in range(len(tree) - len(subTree) + 1):
            if tree[idx: idx + len(subTree)] == subTree:
                return True
        return False
            

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    solution = Solution()
    print(solution.isSubtree(root,subRoot))