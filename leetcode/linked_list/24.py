# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: 50%, Memory: 33%
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        res = ListNode("#") # Dummy head
        res.next = head

        head = res

        while head.next.next != None:
            head = self.swapTwo(head)
            # 在进入下一次循环前检验是否还剩下两个以上节点
            # 避免出现对 None 引用 next 的情况
            if head.next is None: 
                break
        
        return res.next

    # 两两交换
    def swapTwo(self, head: ListNode) -> ListNode:
        # 0->1->2->3->4->^
        first = head.next
        second = head.next.next

        head.next = second
        first.next = second.next
        second.next = first

        return first