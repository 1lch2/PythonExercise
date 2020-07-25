# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1:
# 输入:       1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]
# 输出: true

# 示例 2:
# 输入:      1          1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# 输出: false

# 示例 3:
# 输入:       1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]
# 输出: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 使用广度优先遍历获取序列化的二叉树，再对比返回的序列
# 时间和空间复杂度不太好
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if self.bfs(p) == self.bfs(q):
            return True
        else:
            return False

    def bfs(self, root: TreeNode) -> str:
        if not root:
            return []

        queue = [root]
        res = []
        while len(queue) != 0:
            current = queue.pop(0)
            if current is not None:
                res.append(current.val)
            else:
                res.append(None)

            if current != None:
                queue.append(current.left)
                queue.append(current.right)
        
        return res

# https://leetcode-cn.com/problems/same-tree/solution/hua-jie-suan-fa-100-xiang-tong-de-shu-by-guanpengc/
# 深度优先遍历并比较
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 若当前节点都为空
        if p is None and q is None:
            return True
        # 若当前节点一个为空而一个不为空
        if p is None or q is None:
            return False
        # 若当前节点值不相同
        if p.val != q.val:
            return False
        # 递归进入左右子树并返回结果的与
        # 触发任意截止条件返回布尔值
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)