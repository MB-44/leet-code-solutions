class Solution:
    def findMatrix(nums: list[int]) -> list[list[int]]:
        if len(list(set(nums))) == len(nums):
            return [nums]
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        sortedList = sorted(nums, key=lambda x: (counts[x], x))

        l = len(sortedList)
        




if __name__ == "__main__":
    nums = [1,2,3,4,1,3,1]
    # result = Solution.findMatrix(nums)
    # print(result)