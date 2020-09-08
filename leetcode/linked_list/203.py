# 删除链表中等于给定值 val 的所有节点。

# 示例:

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) 复杂度的遍历法
# Time: 24%, Memory: 71%
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        res = ListNode("#")
        res.next = head
        
        temp = res
        while temp.next != None:
            # 若有值匹配的节点则删除，但是temp不移动
            if temp.next.val == val:
                temp.next = temp.next.next
            else: # 没有匹配节点时向后移一位
                temp = temp.next
        
        return res.next
        

# 递归法
# 还更慢了什么玩意
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 递归终止条件：当前的头节点为空
        if head is None:
            return None
        
        # 进入递归的部分，头节点之后的子链表
        res = self.removeElements(head.next, val)

        # 每层递归的处理
        #* 这部分处理从链表尾部向前连接
        #* # -> 0 -> 1 -> 2 -> 3 -> 4 -> ^
        #*                    head  res
        # 若符合要求则不连接当前头节点，跳过head将res返回给下一层
        if head.val == val: 
            return res
        # 若不符合要求则将子链表接到当前头节点后
        else: 
            head.next = res
            return head