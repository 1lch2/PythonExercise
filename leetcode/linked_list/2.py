# 给出两个 非空 的链表用来表示两个非负的整数。
# 其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        p1, p2 = l1, l2
        res = ListNode(0) # Dummy head
        current = res # 当前计算位置
        carry = 0 # 进位标记

        while p1 != None and p2 != None: # 任意链表遍历到结束时停止
            if p1.val + p2.val + carry >= 10:
                temp = ListNode(p1.val + p2.val + carry - 10)
                carry = 1
            else:
                temp = ListNode(p1.val + p2.val + carry)
                carry = 0

            current.next = temp # 连接到结果链表上
            current = current.next 

            p1 = p1.next
            p2 = p2.next
        
        # 若此时仍有未遍历完的链表
        while p1 != None:
            if p1.val + carry >= 10:
                temp = ListNode(p1.val + carry - 10)
                carry = 1
            else:
                temp = ListNode(p1.val + carry)
                carry = 0
            
            current.next = temp
            current = current.next
            p1 = p1.next

        while p2 != None:
            if p2.val + carry >= 10:
                temp = ListNode(p2.val + carry - 10)
                carry = 1
            else:
                temp = ListNode(p2.val + carry)
                carry = 0

            current.next = temp
            current = current.next
            p2 = p2.next

        # 若此时仍有一位进位
        if carry == 1:
            current.next = ListNode(1)
            carry = 0

        return res.next
