# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 示例：
# 给你这个链表：1->2->3->4->5
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明：
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: 'ListNode', k: int) -> 'ListNode':
        self.k = k
        p = ListNode(-1)
        res = p
        p.next = head
        q = p
        
        # Get length
        temp = head
        l_list = 1
        while temp.next:
            temp = temp.next
            l_list += 1

        for j in range(l_list // k):
            for i in range(k+1):
                q = q.next
            p = self.reverseList(p, q)
            q = p
            
        return res.next


    def reverseList(self, head, tail):
        _tail = tail
        p = head.next

        # 尾插法，将p指向的节点插到尾部
        while p != tail:
            head.next = p.next
            p.next = _tail
            _tail = p
            p = head.next
        # 将head和逆序链表开头连接起来
        head.next = _tail

        for i in range(self.k):
            head = head.next
        return head


if __name__ == "__main__":
    l0 = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    s = Solution()
    res = s.reverseKGroup(l0, 2)

    temp = res
    while temp:
        print(temp.val)
        temp = temp.next