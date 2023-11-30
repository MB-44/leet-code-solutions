class Solution:
    def findDisappearedNumbers(nums):
        disaArray = [i for i in range(1,len(nums+1)) if i not in nums]
        return disaArray

result = Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(result)