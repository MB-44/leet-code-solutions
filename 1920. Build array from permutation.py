class Solution(object):
    def buildArray(self,nums):
        output = [0]*len(nums)
        for i in range(len(nums)):
            output[i] = nums[nums[i]]
        return output


if __name__ == "__main__":
    nums = [5,0,1,2,3,4]
    output = Solution().buildArray(nums)
    print(output)
