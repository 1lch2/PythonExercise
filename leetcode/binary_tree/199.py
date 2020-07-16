# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 示例:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            # l should not be calculated but updated.
            l = len(queue)
            while l:
                c_root = queue[0]

                # add to res only if at the end of each level
                if l == 1:
                    res.append(c_root.val)
                queue.pop(0)
                if c_root.left :
                    queue.append(c_root.left)
                if c_root.right :
                    queue.append(c_root.right)
                
                l -= 1

        return res