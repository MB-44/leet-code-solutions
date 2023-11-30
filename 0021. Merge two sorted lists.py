class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self,list1,list2):
        current = list1
        while current.next is not None:
            current = current.next
        current.next = list2
        
        fullL = []
        while list1 is not None:
            fullL.append(list1.data)
            list1 = list1.next
        fullL.sort()
        
        current = ListNode(fullL[0])

        # while current.next is not None:
        #     current = current.next
        
        for value in fullL[1:]:
            current.next = ListNode(value)
            current = current.next
        return current