class ListNode:
    """Node of a linked list.

    Attributes:
        val: Value of the node.
        next: Pointer of the node, default: None.
    """

    def __init__(self, x: int):
        self.val = x
        self.next = None

    def printnode(self):
        """Print the linked list in string format.

        eg: 1->2->3->null
        """
        # Stop criterion for circular linked lists.
        COUNT = 10
        i = 0
        while self != None and i < COUNT:
            print(str(self.val) + "->", end="")
            self = self.next
            if self == None:
                print("null")
            i += 1

    def reverseList(self):
        """Reverse the linked list.

        Returns: 
            The head node of reversed linked list.
        """
        if self != None:
            stacklist = []
            temp = self
            while temp != None:
                stacklist.append(temp.val)
                temp = temp.next

            node0 = ListNode(stacklist.pop())
            temp = node0
            while len(stacklist) != 0:
                temp.next = ListNode(stacklist.pop())
                temp = temp.next
        else:
            node0 = self

        return node0

    def reverse_dualpointer(self, head):
        """Reverse the linked list in dual pointer method.

        Args:
            head: The head node of linked list.
        Returns:
            The head node of reversed linked list.
        """
        p = None
        q = head
        while q != None:
            temp = q.next
            q.next = p
            p = q
            q = temp

        return p

    @staticmethod
    def mergeTwoLists(l1, l2):
        """Merge two sorted linked lists.

        Args:
            l1: Head node of sorted list one.
            l2: Head node of sorted list two.
        Returns:
            The merged list.
        """
        # Dummy node head
        res = ListNode(0)
        temp = res

        h1, h2 = l1, l2
        while h1 and h2 != None:
            # Compare the next node
            if h1.val <= h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            # Move to current node
            temp = temp.next

        # Dealing with the remaining nodes.
        while h1 or h2 != None:
            if h1 != None:
                temp.next = h1
                h1 = h1.next
                temp = temp.next
            elif h2 != None:
                temp.next = h2
                h2 = h2.next
                temp = temp.next

        return res.next

    @staticmethod
    def listToListNode(seq: list) -> ListNode:
        """Convert a list to a linked list.
        """
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in seq:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr

class DualListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

    # Print out the value of the nodes.
    def printnode(self):
        # Stop criterion for circular linked lists.
        COUNT = 10
        i = 0
        while self != None and i < COUNT:
            if self.pre == None:
                print("null <-> ", end="")
            
            print(str(self.val) + " <-> ", end="")
            self = self.next
            if self == None:
                print("null")
            i += 1


def test_listnode():
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)

    node0.next = node1
    node1.next = node2

    node0.printnode()
    temp = node0
    temp.next.printnode()

    # Reverse list
    newlist = node0.reverseList()
    newlist.printnode()

    # Merge two lists
    merged = ListNode.mergeTwoLists(node0, newlist)
    merged.printnode()

    # Circular linked list
    node2.next = node0
    node0.printnode()


def test_dual_listnode():
    node0 = DualListNode(0)
    node1 = DualListNode(1)
    node2 = DualListNode(2)

    node0.next = node1
    node1.next = node2
    node2.pre = node1
    node1.pre = node0

    node0.printnode()


if __name__ == '__main__':
    test_dual_listnode()
