class Solution:
    def smallerNumbersThanCurrent(nums):
        l = len(nums)
        countNums = [0]*l
        for i in range(l):
            if max(nums) == nums[i]:
                countNums[i] = l-1
            elif min(nums) == nums[i]:
                countNums[i] == 0
                



if __name__ == "__main__":
    pass
        