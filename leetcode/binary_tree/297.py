# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，
# 进而可以将转换后的数据存储在一个文件或者内存中，
# 同时也可以通过网络传输到另一个计算机环境，
# 采取相反方式重构得到原数据。

# 请设计一个算法来实现二叉树的序列化与反序列化。
# 这里不限定你的序列 / 反序列化算法执行逻辑，
# 你只需要保证一个二叉树可以被序列化为一个字符串，
# 并且将这个字符串反序列化为原始的树结构。

# 示例: 
# 你可以将以下二叉树：
#     1
#    / \
#   2   3
#      / \
#     4   5

# 序列化为 "[1,2,3,null,null,4,5]"
# 提示: 
# 这与 LeetCode 目前使用的方式一致，
# 详情请参阅 LeetCode 序列化二叉树的格式。
# 你并非必须采取这种方式，
# 你也可以采用其他的方法解决这个问题。

# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，
# 你的序列化和反序列化算法应该是无状态的。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == "__main__":
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

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7
    node7.left = node8

    codec = Codec()
    tree_str = codec.serialize(root)
    tree = codec.deserialize(tree_str)
    print(tree_str)

    queue = [tree]
    while len(queue) != 0:
        current = queue.pop(0)
        print(current.val, end=" -> ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
