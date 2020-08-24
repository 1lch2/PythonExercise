# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6

# 示例 2：
# 输入：lists = []
# 输出：[]

# 示例 3：
# 输入：lists = [[]]
# 输出：[]

# 提示：
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4

# Definition for singly-linked list.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 分治法
# Time: 23.35%, Memory: 58.62%
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        subNum = len(lists)

        if subNum == 0:
            return None
        
        # 两两合并
        interval = 2
        while interval <= subNum:
            for i in range(len(lists) // 2): # 每次更新合并次数
                l1 = lists.pop(0)
                l2 = lists.pop(0)

                new = self.mergeTwoLists(l1, l2)
                lists.append(new)
            interval *= 2
        
        # 当链表数量不是偶数时多合并最后一次
        if len(lists) != 1:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode("#")
        temp = res

        h1, h2 = l1, l2
        while h1 != None and h2 != None:
            if h1.val <= h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            
            temp = temp.next
        
        while h1 != None or h2 != None:
            if h1 != None:
                temp.next = h1
                h1 = h1.next
                temp = temp.next

            if h2 != None:
                temp.next = h2
                h2 = h2.next
                temp = temp.next
        
        return res.next
