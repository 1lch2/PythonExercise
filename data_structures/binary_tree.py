class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    # Add new node to existing tree node.
    def add(self, node, side):
        if side == 'l':
            self.left = node
        elif side == 'r':
            self.right = node
        else:
            raise(Exception('Wrong parameter.'))
        

    # Depth first search, a.k.a., preorder traversal.
    def dfs(self, root):
        if self.val == None:
            print('Empty tree.')
        else:
            print(root.val, end=' -> ')
            if root.left != None:
                self.dfs(root.left)
            if root.right != None:
                self.dfs(root.right)


if __name__ == '__main__':
    # Test case: root
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    
    root.add(node1, 'l')
    root.add(node2, 'r')
    node1.add(node3, 'l')
    node1.add(node4, 'r')
    node2.add(node5, 'r')

    root.dfs(root)
