class Solution(object):
    def getConcatenation(self,nums):
        nums2 = nums
        nums.extend(nums2)
        return nums

if __name__ == "__main__":
    nums = [1,2,1]
    result = Solution().getConcatenation(nums)
    print(result)