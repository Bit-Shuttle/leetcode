from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    二叉树的层次遍历（BFS）
    返回每个层级的节点值列表
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# 测试用例
if __name__ == "__main__":
    # 测试用例1: 标准二叉树
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print("测试用例1:")
    print(levelOrder(root1))  # 预期输出: [[3], [9, 20], [15, 7]]
    
    # 测试用例2: 空树
    root2 = None
    print("\n测试用例2 (空树):")
    print(levelOrder(root2))  # 预期输出: []
    
    # 测试用例3: 单节点树
    root3 = TreeNode(1)
    print("\n测试用例3 (单节点):")
    print(levelOrder(root3))  # 预期输出: [[1]]
    
    # 测试用例4: 只有左子树的树
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    print("\n测试用例4:")
    print(levelOrder(root4))  # 预期输出: [[1], [2], [3]]

    # 测试用例5: q124 Binary Tree Maximum Path Sum
    from q124 import Solution

    root5 = TreeNode(-2)
    root5.right = TreeNode(-3)
    sol = Solution()
    result = sol.maxPathSum(root5)
    print("\n测试用例5 (q124):")
    print(f"最大路径和: {result}")  # 预期输出: -2
