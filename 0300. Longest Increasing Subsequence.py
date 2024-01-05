class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        for j in range(1,n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i] + 1, dp[j])
        return max(dp)