class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        end = 0

        for start in range(n):
            while end < n and (end == start or nums[end] > nums[end - 1]):
                end += 1    
            result += (end - start)
        
        return result