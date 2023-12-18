class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        a,c = max(nums), min(nums)
        nums.remove(a), nums.remove(c)
        b,d = max(nums), min(nums)
        return (a * b) - (c * d)
    

# or
    
class Solution:
    def maxProductDifference(self,nums: list[int]) -> int:
        a, c = max(nums), min(nums)
        nums.remove(a), nums.remove(c)
        return (a * max(nums)) - (c * min(nums))    