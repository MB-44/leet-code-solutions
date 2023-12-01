class Solution:
    def findNonMinOrMax(nums):
        n = -1
        maxVal,minVal = max(nums), min(nums)
        for i in nums:
            if maxVal != i  and minVal != i:
                return i
        return -1
        