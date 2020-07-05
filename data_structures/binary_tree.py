class TreeNode(object):
    """Node of a binary tree.

    Attributes:
        val: The value of the node.
        left: Left child of current node, default: None.
        right: Right child of current node, default: None.
    """

    def __init__(self, val: int) -> "TreeNode":
        """Initialize the TreeNode with desired value.

        Args:
            val: The value of the tree node.
        """
        self.val = val
        self.left = None
        self.right = None

    def add(self, node: "TreeNode", side: str):
        """Add new node to existing tree node.

        Args:
            node: The node to be added to the tree.
            side: The side that the node is added to. "l" for left side, "r" for right side.
        Returns:
            No return, the operation is on the original TreeNode object.
        """
        if side == 'l':
            self.left = node
        elif side == 'r':
            self.right = node
        else:
            raise(Exception('Wrong parameter.'))

    def dfs(self, root: "TreeNode", mode="recursive"):
        """Depth first search, a.k.a., preorder traversal.

        Args:
            root: Root node of the binary tree.
            mode: Traversal mode. "recursive" for using recursive method, "stack" for using stack method.
        Returns:
            No returns, only print out the value of the nodes in the traversal sequence.
        """
        if self.val == None:
            print('Empty tree.')
        else:
            if mode == "recursive":
                print(root.val, end=' -> ')
                if root.left != None:
                    self.dfs(root.left)
                if root.right != None:
                    self.dfs(root.right)
            elif mode == "stack":
                stack = []
                stack.append(root)
                while len(stack) > 0:
                    current_root = stack[-1]
                    print(current_root.val, end=" -> ")
                    stack.pop()
                    if current_root.right != None:
                        stack.append(current_root.right)
                    if current_root.left != None:
                        stack.append(current_root.left)

    def bfs(self, root: "TreeNode"):
        """Breadth-first traversal.

        Args:
            root: Root node of the binary tree.
        Returns:
            No returns, only print out the value of the nodes in the traversal sequence.
        """
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current_root = queue[0]
            print(current_root.val, end=" -> ")
            queue.pop(0)
            if current_root.left != None:
                queue.append(current_root.left)
            if current_root.right != None:
                queue.append(current_root.right)


def test_binary_tree():
    # Test case: root
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    #        / \
    #       6   7

    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    root.add(node1, 'l')
    root.add(node2, 'r')
    node1.add(node3, 'l')
    node1.add(node4, 'r')
    node2.add(node5, 'r')
    node5.add(node6, 'l')
    node5.add(node7, 'r')

    root.dfs(root, mode="stack")
    print("\n")
    root.bfs(root)


if __name__ == '__main__':
    test_binary_tree()
