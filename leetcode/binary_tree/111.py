# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 当前根节点为空，则当前层数为 0
        if root is None:
            return 0
        # 当前为叶子节点，则当前层数为 1
        if root.left is None and root.right is None:
            return 1
        # 若并非叶子节点，则进入子树
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 若当前节点中有一个子节点为空，即 left 或 right 有一个为 0
        # 则返回非空的子树的深度：left + right + 1
        if root.left is None or root.right is None:
            return left + right + 1

        # 若以上皆不成立，则直接返回当前最小的子树深度 + 1
        return min(left, right) + 1
