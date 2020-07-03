# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def delete_node(self, node):
        # Idea: Delete the next node, but perserve the value of its next node to achieve the same result.
        node.val = node.next.val
        node.next = node.next.next
