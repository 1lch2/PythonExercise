# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# 进阶：
# 你可以运用递归和迭代两种方法解决这个问题吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #* 使用递归，仅关注当前处理的根节点和直接子节点两层
        #* 然后考虑进入递归和退出递归的条件
        if root is None:
            return True
        
        return self.check(root.left, root.right)

    
    def check(self, left: TreeNode, right: TreeNode) -> bool:
        # 若左右子树均为空，则显然对称
        if left is None and right is None:
            return True
        
        # 若左右子树仅有一个为空，显然不对称
        if left is None or right is None:
            return False
        
        # 若左右节点均不为空但值不相同，显然不对称
        if left.val != right.val:
            return False

        # 若没有到达空的叶子节点，且当前子节点均对称，则进入各自的对称左右节点继续判断
        return self.check(left.left, right.right) and self.check(left.right, right.left)


# 迭代法
# Time: 99%, Memory: 21%
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = [root.left, root.right]

        while len(queue) != 0:
            currentLen = len(queue)
            while currentLen != 0:
                left = queue.pop(0)
                right = queue.pop(0)

                # 判断逻辑同递归版
                # 若已经到达空叶子节点，则跳过压入队列操作
                if left is None and right is None: 
                    currentLen -= 2 # 跳过前修改判断变量
                    continue
                elif left is None or right is None:
                    return False
                elif left.val != right.val:
                    return False
                
                # 按对称位置将子节点压入队列
                queue.extend([left.left, right.right])
                queue.extend([left.right, right.left])

                currentLen -= 2

        return True
