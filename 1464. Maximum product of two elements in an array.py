class Solution:
    def maxProduct(nums: list[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        return (max1-1)*(max2-1)



if __name__ == "__main__":
    nums = [3,4,5,2]
    result = Solution.maxProduct(nums)
    print(result)