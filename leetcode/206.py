# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

    def printnode(self):
        while self != None:
            print(self.val)
            self = self.next


# High memory cost.
class Solution0:
    def reverseList(self, head: ListNode) -> ListNode:
        if head != None:
            stacklist = []
            temp = head
            while temp != None:
                stacklist.append(temp.val)
                temp = temp.next
            
            node0 = ListNode(stacklist.pop())
            temp = node0
            while len(stacklist) != 0:
                temp.next = ListNode(stacklist.pop())
                temp = temp.next
        else:
            node0 = head

        return node0


# Dual pointer solution.
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        q = head
        while q != None:
            temp = q.next
            q.next = p
            p = q
            q = temp
        
        return p

# Python怎么写也不会跑得比C快
