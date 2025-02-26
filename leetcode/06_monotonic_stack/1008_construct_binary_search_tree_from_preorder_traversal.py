from typing import List

class TreeNode:
    def __int__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        