# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
