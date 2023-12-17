# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head):
        current, length = head, 0
        while current is not None:
            length += 1
            current = current.next
        current = head
        midId = (length//2)+1
        while midId > 1:
            current = current.next
            midId -= 1
        return current




        