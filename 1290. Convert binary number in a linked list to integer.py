class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def getDecimalValue(self,head: ListNode)->int:
        str = ""
        num = head
        while num is not None:
            str += num.val
            num = num.next
        dec,x = 0,0
        for i in str[::-1]:
            dec += (2**x)*int(i)
            x += 1
        return dec

        