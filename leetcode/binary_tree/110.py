# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://lyl0724.github.io/2020/01/25/1/
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if self.judgeTree(root) == -1:
            return False
        else:
            return True
            
    # 递归操作
    def judgeTree(self, root: TreeNode) -> int:
        # 遍历终止条件：到达叶子节点
        # 以叶子节点的空节点为根的树深度为 0
        if root is None:
            return 0

        # 递归进入左右子树获得树的深度
        left = self.judgeTree(root.left)
        right = self.judgeTree(root.right)

        # 返回值 -1 代表该子树不是二叉平衡树
        # 若左右任一子树不是二叉平衡树，则当前树不是二叉平衡树
        if left == -1 or right == -1:
            return -1
        # 若左右树高度差大于 1，则当前树不是二叉平衡树
        if abs(left - right) > 1:
            return -1
        
        # 若以上条件均不成立，则返回当前树的最大深度
        # 即，左右子树最大的深度加上当前根节点（+1）
        return max(left, right) + 1