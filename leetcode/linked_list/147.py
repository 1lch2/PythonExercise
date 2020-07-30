# 插入排序算法：

# 插入排序是迭代的，每次只移动一个元素，
# 直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，
# 找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#  
# 示例 1：
# 输入: 4->2->1->3
# 输出: 1->2->3->4

# 示例 2：
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        pre = ListNode("#") # Dummy node
        pre.next = head

        ordered = head # Currently ordered part
        current = head.next
        # Traverse the list
        while current is not None:
            # If current node value is greater than last one.
            if current.val > ordered.val:
                ordered = ordered.next
                current = current.next
            else:
                temp = pre
                # Find the interval
                while temp.next.val < current.val:
                    temp = temp.next
                # Insert the node
                ordered.next = current.next
                current.next = temp.next
                temp.next = current

                # Relocate current pointer
                current = ordered.next

        return pre.next
