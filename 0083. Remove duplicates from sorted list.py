class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
    
class Solution:
    def deleteDuplicates(self,head):
        values = []
        current = head
        while current:
            values.append(current.value)
            current = current.next
        
        values = sorted(list(set(values)),reverse=True)

        newHead = None
        for value in values:
            newHead = ListNode(value,newHead)
        return newHead