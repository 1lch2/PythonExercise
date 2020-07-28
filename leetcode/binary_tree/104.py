# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# BFS
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = [root]
        dep = 0
        while len(queue) != 0:
            l = len(queue)
            while l :
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                l -= 1
            if l == 0:
                dep += 1
        return dep