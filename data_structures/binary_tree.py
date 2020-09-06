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
            mode: Traversal mode. 
                  "recursive" for using recursive method;
                  "stack" for using stack method.
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
        queue.append(root) # 创建队列并压入根节点
        while len(queue) > 0:
            current_root = queue[0]
            print(current_root.val, end=" -> ")
            queue.pop(0)
            if current_root.left != None:
                queue.append(current_root.left)
            if current_root.right != None:
                queue.append(current_root.right)
    
    def inorder(self, root: "TreeNode", mode="stack"):
        """Inorder traversal.

        Args:
            root: Root node of the binary tree.
            mode: Traversal mode. 
                  "recursive" for using recursive method;
                  "stack" for using stack method;
        Returns:
            No returns, only print out the value of the nodes in the traversal sequence.
        """
        if root is None:
            print("Empty tree!")
            return
        if mode == "stack":
            # Credit: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
            # 使用不同颜色标记已经访问过的和未访问的节点
            WHITE = 0 # 白色为新节点
            GREY = 1 # 灰色为已经访问过的节点

            # 若遇到的节点为白色，则将其标记为灰色，然后将右节点，自身，左节点依次入栈
            # 若遇到的节点为灰色，则输出它的值
            #* 颜色标记的思路三种遍历都通用
            #* 可以改用类型判断而不是使用元组，节点类型则进入并压栈，值类型则访问输出
            stack = [(WHITE, root)]
            while stack:
                color, current = stack.pop() # 弹出栈顶元素
                if current is None: # 遍历中会出现将叶子节点的左右空节点压入栈的情况
                    continue # 跳过后续操作来弹出空的叶子节点
                if color == WHITE: # 若节点未被访问过
                    stack.append((WHITE, current.right))
                    stack.append((GREY, current))
                    stack.append((WHITE, current.left))
                else: # if color == GREY
                    print(current.val, end=" -> ") # 此处为节点访问操作
        elif mode == "recursive":
            if root.left != None:
                self.inorder(root.left, mode="recursive")
            print(root.val, end=" -> ") # 节点访问操作
            if root.right != None:
                self.inorder(root.right, mode="recursive")
        else:
            raise(ValueError("Wrong parameter!"))
            
class BinTreeCodec:
    """Encode and decode a binary tree.
    """
    
    @classmethod
    def serialize(cls, root: "TreeNode"):
        """Encodes a tree to a single string.
        
        Args:
            root: Root node of the binary tree
        Returns:
            A serialized string of the input tree.
        """
        if root is None:
            return "[]"
        queue = [root]
        res = []
        while len(queue) != 0:
            current = queue[0]
            if isinstance(current, TreeNode):
                res.append(current.val)
            else:
                res.append(current)

            queue.pop(0)
            if current != None: # 把空的子节点也加入队列
                queue.append(current.left)
                queue.append(current.right)
        
        # Remove the None in tail.
        for i in range(len(res)-1, -1, -1):
            if res[i] != None:
                res = res[:i+1]
                break
        return str(res)
        
    @classmethod
    def deserialize(cls, data: str):
        """Decodes your encoded data to tree.
        
        Args:
            data: A serialized string of tree.
        Returns:
            The root node of the binary tree.
        """
        l = eval(data) # 解析list字符串
        if len(l) == 0:
            return None

        root = TreeNode(l[0]) # root node
        queue = [root] # 建立队列并将root压入队列

        i = 0
        # 广度优先遍历添加节点
        # 广度优先添加节点和遍历二叉树逻辑相同
        # current标记当前父节点，依次更新下标将非空的子节点加入
        while len(queue) != 0:
            current = queue.pop(0)
            i += 1 # 添加左节点
            if i < len(l):
                if l[i] != None:
                    current.left = left = TreeNode(l[i])
                    queue.append(left)
            i += 1 # 添加右节点
            if i < len(l):
                if l[i] != None:
                    current.right = right = TreeNode(l[i])
                    queue.append(right)

        return root


def test_binary_tree():
    # Test case: root
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    #        / \
    #       6   7
    #          / 
    #         8
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    root.add(node1, 'l')
    root.add(node2, 'r')
    node1.add(node3, 'l')
    node1.add(node4, 'r')
    node2.add(node5, 'r')
    node5.add(node6, 'l')
    node5.add(node7, 'r')
    node7.add(node8, 'l')

    root.dfs(root, mode="stack")
    print("\n")
    root.bfs(root)
    print("\n")
    root.inorder(root, mode="stack")
    print("\n")
    root.inorder(root, mode="recursive")
    print('\n')

    print("serialized tree")
    tree_str = BinTreeCodec.serialize(root)
    print(tree_str)
    tree = BinTreeCodec.deserialize(tree_str)
    tree.bfs(tree)

if __name__ == '__main__':
    test_binary_tree()
