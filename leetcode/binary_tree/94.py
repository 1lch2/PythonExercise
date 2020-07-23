# 给定一个二叉树，返回它的中序 遍历。

# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, grey = 0, 1
        stack = [(white, root)]
        res = []
        while stack:
            color, current = stack.pop()
            if current is None:
                continue
            if color == white:
                stack.append((white, current.right))
                stack.append((grey, current))
                stack.append((white, current.left))
            else:
                res.append(current.val)
        return res
