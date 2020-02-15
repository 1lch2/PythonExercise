class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Depth first search, a.k.a., preorder traversal.
    def dfs(self, root):
        if self.val == None:
            print('Empty tree.')
        else:
            print(root.val)
            if root.left != None:
                self.dfs(root.left)
            if root.right != None:
                self.dfs(root.right)


if __name__ == '__main__':
    # Test case: root
    #     0
    #    / \
    #   1   2
    #  / \
    # 3   4
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    root.dfs(root)
