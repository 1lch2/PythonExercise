# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true

# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Time: 89%, Memory: 67%
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.judgeTree(root)
    
    def judgeTree(self, root: TreeNode, lower=float("-inf"), upper=float("inf")) -> bool:
        #* 为节点的比较上下界设置默认值
        #* 每次比较本节点和它的父节点而不是向下比较
        
        #* e.g.:
        #* 左节点一定小于它的父节点，则将上界设为父节点，下界维持默认的负无穷

        # 若到达为空的叶子节点，显然是BST
        if root is None:
            return True
        
        # 若非叶子节点时
        rootVal = root.val       
        if rootVal <= lower or rootVal >= upper:
            return False

        # 递归进入左右子树判断
        return self.judgeTree(root.left, lower, rootVal) and self.judgeTree(root.right, rootVal, upper)

if __name__ == "__main__":
    S = Solution()

    root = TreeNode(1)
    l1 = TreeNode(1)
    root.left = l1

    print(S.isValidBST(root))