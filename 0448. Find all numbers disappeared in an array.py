class Solution:
    def findDisappearedNumbers(nums):
        data = {}
        for d in nums:
            data[d] = True
        
        disaArr = []
        for i in range(1, len(nums) + 1):
            if i not in data.keys():
                disaArr.append(i)
        return disaArr


if __name__ == "__main__":
    result = Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(result)