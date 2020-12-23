# 给定一个二叉树，返回它的 后序 遍历。

# 示例:
# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代方法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack = [root]
        res = []
        while stack:
            current = stack.pop()
            if current is None:
                continue
            # 按反序压入当前根节点的值和左右节点指针
            if isinstance(current, TreeNode):
                stack.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
            else: # 若弹出的栈顶元素不为节点，则已经访问过，直接访问其值
                res.append(current)
        return res
        

if __name__ == "__main__":
    # Test case: root
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    #        / \
    #       6   7
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    S = Solution()
    print(S.postorderTraversal(root))