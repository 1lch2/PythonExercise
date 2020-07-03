# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

# 示例 1:

# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Simple idea of combining dfs and quicksort.
# High time and memory cost.
class Solution0:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(root, res):
            res.append(root.val)
            if root.left != None:
                dfs(root.left, res)
            if root.right != None:
                dfs(root.right, res)
        res = []
        dfs(root, res)

        def quicksort(seq, low, high):
            i = low
            j = high
            
            if low < high:
                base = seq[low]
                while i < j:
                    while seq[j] > base and j > i:
                        j -= 1
                    if j > i:
                        seq[i] = seq[j]
                        i += 1
                    
                    while seq[i] < base and i < j:
                        i += 1
                    if i < j:
                        seq[j] = seq[i]
                        j -= 1
                    
                seq[i] = base

                quicksort(seq, low, i-1)
                quicksort(seq, i+1, high)
        
        quicksort(res, 0, len(res)-1)
        return res[k-1]


# Inorder traversal.
class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root, res):
            if root.left != None:
                inorder(root.left, res)
            res.append(root.val)
            if root.right != None:
                inorder(root.right, res)
        
        res = []
        inorder(root, res)
        return res[k-1]
