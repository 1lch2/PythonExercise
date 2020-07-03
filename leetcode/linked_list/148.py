# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# 示例 1:
# 输入: 4->2->1->3
# 输出: 1->2->3->4

# 示例 2:
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Added myself, not in the official question.
    def printnode(self):
        while self != None:
            print(str(self.val) + "->", end="")
            self = self.next
            if self == None:
                print("null")


# https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # # If input is empty
        # if head or head.next is None:
        #     return head
        
        # Get the length of linked list
        list_len = 0
        temp = head
        while temp:
            temp = temp.next
            list_len += 1

        # Dummy head, linked before the list
        res = ListNode(0)
        res.next = head

        intv = 1
        while intv < list_len:
            pre = res
            temp = res.next

            while temp:
                # Get h1 list
                h1 = temp
                i = intv

                # Get h2 list
                while i > 0 and temp != None:
                    temp = temp.next
                    i -= 1
                if i > 0:
                    break
                h2 = temp
                i = intv

                # Get the length of h1, h2
                while i > 0 and temp != None:
                    temp = temp.next
                    i -= 1
                c1 = intv
                c2 = intv - i

                # Merge two lists
                while c1 > 0 and c2 > 0:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next

                # Link the rest one
                if c1 > 0:
                    pre.next = h1
                else:
                    pre.next = h2
                
                # Link the remaining nodes.
                while c1 > 0 or c2 > 0:
                    pre  = pre.next
                    c1 -= 1
                    c2 -= 1
                
                pre.next = temp

            intv *= 2

        return res.next

if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(2)
    d = ListNode(1)

    a.next = b
    b.next = c
    c.next = d

    a.printnode()

    x = Solution()
    w = x.sortList(a)

    w.printnode()