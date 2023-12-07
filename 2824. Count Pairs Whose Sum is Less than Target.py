class Solution:
    def countPairs(nums: list[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if (nums[i] + nums[j]) < target:
                    count += 1
        return count