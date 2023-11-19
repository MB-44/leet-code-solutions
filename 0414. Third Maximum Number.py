# 30ms

class Solution(object):
    def thirdMax(self,nums):
        sortedArray = sorted(list(set(nums)), reverse=True)
        if len(sortedArray) < 3:
            return max(sortedArray)
        return sortedArray[2]
