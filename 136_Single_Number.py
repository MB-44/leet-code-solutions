# 136. Single Number 
# Mode - Easy
# Array / Bit Manipulation

# Runtime - 2537ms
# Memory - 16.1 MB

def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    nonNum = list(set(nums))
    for num in nonNum:
        if nums.count(num) == 1:
            return num
     
        # D:\python\leet code\.git\136. Single Number.py
        #D:\python\leet code\136. Single Number.py