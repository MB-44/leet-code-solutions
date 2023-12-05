
#45ms
class Solution:
    def isSameAfterReversals(num: int) -> bool:
        if num < 10:
            return True
        return ((str(num)[::-1]).strip("0"))[::-1] == str(num)


#32ms - more accurate
class Solution:
    def isSameAfterReversals(self,num: int) -> bool:
        if num < 10:
            return True
        if num%10 == 0:
            return False
        else: 
            return True
