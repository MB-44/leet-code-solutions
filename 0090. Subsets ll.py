class Solution(object):
    def subsetsWithDup(self,nums):
        subsets = [[]]
        if len(nums) == 1:
            subsets.append(nums[0])
        else: 
            for i in range(len(nums)-1):
                for j in range(i,len(nums)):
                    subsets.append(nums[i:j+1])
        return subsets

if __name__ == "__main__":
    nums = [1,2,2]
    result = Solution().subsetsWithDup(nums)
    print(result)