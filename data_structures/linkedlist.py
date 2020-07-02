class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Print the linked list in string format
    # eg: 1->2->3->null
    def printnode(self):
        while self != None:
            print(str(self.val) + "->", end="")
            self = self.next
            if self == None:
                print("null")
    
    # Reverse the linked list.
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

    # Reverse the linked list in dual pointer method.
    def reverse_dualpointer(self, head):
        p = None
        q = head
        while q != None:
            temp = q.next
            q.next = p
            p = q
            q = temp
        
        return p
    
    # Merge two sorted linked lists.
    @staticmethod
    def mergeTwoLists(l1, l2):
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

    merged = ListNode.mergeTwoLists(node0, newlist)
    merged.printnode()

if __name__ == '__main__':
    test_listnode()
