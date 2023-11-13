# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]):
        for i in range(len(nums)):
            if nums[i] is None:
                nums.remove(nums[i])
                nums.insert(len(nums),0)
            continue

