# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 
# （即逐层地，从左到右访问所有节点）。

# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []
        while len(queue) > 0:
            l = len(queue) # l 延迟更新
            temp = []
            while l > 0: # 遍历当前一层长度内的节点
                current = queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                l -= 1

            res.append(temp)
        return res

if __name__ == "__main__":
    node0 = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    node0.left = node1
    node0.right = node2
    node2.left = node3
    node2.right = node4

    S = Solution()
    print(S.levelOrder(node0))
