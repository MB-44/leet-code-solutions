class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        startPoint, endPoint = [-1,-1]
        if nums.count(target) == 1:
            return [nums.index(target),nums.index(target)]
        if target not in nums:
            return startPoint, endPoint
        start = end = False
        for i in range(len(nums)):
            if nums[i] == target and start == False:
                startPoint = i
                start = True
            if nums[i] == target and end == False:
                endPoint = i
        return startPoint, endPoint