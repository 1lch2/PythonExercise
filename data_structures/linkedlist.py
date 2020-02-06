class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printnode(self):
        while self != None:
            print(self.val)
            self = self.next
    

    def reverseList(self):
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


def reverse_dualpointer(self, head: ListNode) -> ListNode:
    p = None
    q = head
    while q != None:
        temp = q.next
        q.next = p
        p = q
        q = temp
    
    return p


def test_listnode():
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)

    node0.next = node1
    node1.next = node2

    node0.printnode()
    temp = node0
    temp.next.printnode()

    newlist = node0.reverseList()
    newlist.printnode()


if __name__ == '__main__':
    test_listnode()
