class Solution(object):
    def findDuplicate(self, nums):
        for num in nums:
            if nums.count(num) >= 2:
                return num
        
# Correct, But need to be optimized