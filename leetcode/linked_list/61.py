# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL

# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL

# 示例 2:
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL

# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: 77%, Memory: 47%
# O(2n)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None:
            return head

        # 获取链表长度
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1

        k = k % length # 取余

        temp = head
        res = ListNode("#") # Dummy head

        # 定位新的头节点
        for i in range(length - k - 1):
            temp = temp.next
        
        res.next = temp.next # 连接新的头节点
        temp.next = None # 断开链表

        # 定位连接处
        temp = res
        for i in range(k):
            temp = temp.next
        
        temp.next = head # 连接旧的头节点

        return res.next