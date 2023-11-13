class Solution:
    def twoSum(self, nums: list[int], target: int):
        sum = nums[0]
        for i in range(1,len(nums)):
            sum += nums[i]
            if sum == target:
                ex = [i for i in range(nums.index(nums[i-1]),i+1)]
                return ex
                break
            sum -= nums[i-1] 
        

ex = Solution().twoSum([2,7,11,15],9)
print(ex)