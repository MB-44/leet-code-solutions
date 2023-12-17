# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, value):
        if not head:
            return None

        while head and head.val == value:
            head = head.next

        current = head
        while current and current.next:
            if current.next.val == value:
                current.next = current.next.next
                continue
            current = current.next
        return current