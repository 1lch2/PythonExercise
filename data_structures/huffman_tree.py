class HuffmanTreeNode(object):
    """Node of a Huffman tree.

    Attributes:
        char: The assigned character for the node.
        code: The code for Huffman encoding of the node, default:0. Value is assigned with 0 or 1.
        left: Left child of current node, default: None.
        right: Right child of current node, default: None.
    """
    
    def __init__(self, char: str, code: int):
        """Initialize the Huffman tree node with assigned character and node value.

        Args:
            char: The assigned character for the node.
            code: The code for Huffman encoding of the node, default:0. Value can be assigned with 0 or 1.
        """
        self.char = char
        self.code = code
        self.left = None
        self.right = None


class HuffmanTree(object):
    """Huffman tree object.

    Attributes:
        sorted_list: character and its frenquency in ascending order.
        root_node: Root node of the Huffman tree.
    """

    def __init__(self, seq: str):
        """Huffman tree encoding for a string sequence.

        Args: 
            Input string with more than 2 different characters.
        Returns:
            Root node of the Huffman tree.
        """

        seq_list = list(seq)
        # Exceptions
        if len(set(seq_list)) <= 2:
            print("The input string should have more than 2 different characters.")
            raise Exception(ValueError)

        char_count = {}

        # Count the number of occurance for each character.
        for key in seq_list:
            char_count[key] = char_count.get(key, 0) + 1
        
        # Ref: https://blog.csdn.net/tangtanghao511/article/details/47810729
        self.sorted_list = sorted(char_count.items(), key=lambda item: item[1])

        # Bottom leaves child of the Huffman tree.
        lnode = HuffmanTreeNode(self.sorted_list[0][0], 0)
        rnode = HuffmanTreeNode(self.sorted_list[1][0], 1)
        self.root_node = HuffmanTreeNode("", 1)
        self.root_node.left = lnode
        self.root_node.right = rnode

        # Build Huffman tree and encoding the node from bottom up.
        for tp in self.sorted_list[2:]:
            lnode = HuffmanTreeNode(tp[0], 0)
            rnode = self.root_node

            self.root_node = HuffmanTreeNode("", 1)
            self.root_node.left = lnode
            self.root_node.right = rnode

    def get_encoding(self):
        """Print out the Huffman encoding
        """
        coding_dict = {}
        for ch in self.sorted_list:
            coding_dict[ch[0]] = []
            temp = self.root_node
            coding = []
            while temp.right != None:
                if temp.left.char == ch[0]:
                    coding.append(temp.left.code)
                    break
                elif temp.right.char == ch[0]:
                    coding.append(temp.right.code)
                    break
                coding.append(temp.right.code)
                temp = temp.right

            coding_dict[ch[0]] = coding
        
        print(coding_dict)


def test_huffman_tree():
    seq = "AAABBACCCDEEA"
    hftree = HuffmanTree(seq)
    hftree.get_encoding()

if __name__ == "__main__":
    test_huffman_tree()