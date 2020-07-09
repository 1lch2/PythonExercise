# 给定一个二叉树，返回它的 前序 遍历。

#  示例:

# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://github.com/SleepwalkerCh/Leetcode-/blob/master/144.py
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# Stack solution
class Solution_:
    def preorderTraversal(self, root: 'TreeNode') -> List[int]:
        if root:
            stack = []
            stack.append(root)
            res = []
            while len(stack) > 0:
                current = stack[-1]
                res.append(current.val)
                stack.pop()
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            return res
        else:
            return []