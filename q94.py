# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1: 空树
    print("测试用例1 - 空树:", solution.inorderTraversal(None))
    
    # 测试用例2: 只有一个节点的树
    root1 = TreeNode(1)
    print("测试用例2 - 单节点:", solution.inorderTraversal(root1))
    
    # 测试用例3: 完整的二叉树
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    print("测试用例3 - 完整二叉树:", solution.inorderTraversal(root2))
    
    # 测试用例4: 只有左子树的树
    #     1
    #    /
    #   2
    #  /
    # 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    print("测试用例4 - 只有左子树:", solution.inorderTraversal(root3))
    
    # 测试用例5: 只有右子树的树
    #   1
    #    \
    #     2
    #      \
    #       3
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    print("测试用例5 - 只有右子树:", solution.inorderTraversal(root4))
