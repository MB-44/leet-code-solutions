class Solution(object):
    def firstMissingPositive(self,nums):
        if (1 not in nums):
            return 1
        fullList = [i for i in range(2,max(nums)+1)]
        for n in fullList:
            if n not in nums:
                return n
        return max(nums)+1


if __name__ == "__main__":
    nums = [3,4,-1,1]
    x = Solution().firstMissingPositive(nums)
    print(x)