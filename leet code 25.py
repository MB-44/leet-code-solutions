class Solution:
    def permute(self, nums: list[int]):
        numStr = ""
        for letter in nums:
            numStr += str(letter)
        

x = Solution().permute([1,2,3])
print(x)