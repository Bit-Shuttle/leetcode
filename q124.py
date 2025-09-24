# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = -1001
    def fun(self,node):
        if not node:
            return 0
        left = max(self.fun(node.left), 0)
        right = max(self.fun(node.right), 0)
        self.ans=  max(self.ans, left + right + node.val)
        return max(max(left,right),0)+ node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.fun(root.left)
        left = max(0,left)
        right = self.fun(root.right)
        right = max(0, right)
        self.ans = max(self.ans, left + right + root.val)
        return self.ans


root5 = TreeNode(-2)
root5.right = TreeNode(-3)
sol = Solution()
sol.maxPathSum(root5)