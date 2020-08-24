# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.

# 说明：
# 给定的 n 保证是有效的。

# 进阶：
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hashmap method
# Time: 34.47%, Memory: 89.67%
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        res = ListNode(0) # Dummy head
        res.next = head

        hashMap = {-1: res}

        temp = res.next
        i = 0
        while temp != None:
            hashMap[i] = temp
            temp = temp.next
            i += 1
        
        temp = hashMap[i-n-1]
        temp.next = hashMap[i-n].next
        return res.next
    

# Dual pointer method
# Time: 60.54%, Memory: 50.08%
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        res = ListNode(0) # Dummy head
        res.next = head

        first = res 
        second = res

        # 让 first 和 second 相距 n+1 个节点
        for i in range(n+1):
            first = first.next
            
        # 当first到达尾部时，second位置就是要删除节点的位置的前驱
        while first != None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return res.next