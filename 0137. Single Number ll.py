# 137. Single Number ll
# Medium 
# Arrays | Bit manipulation

def singleNumber(nums):
    uniqueNums = list(set(nums))
    for num in uniqueNums:
        if nums.count(num) == 1:
            return num
        
def singleNumber(nums):
    for i in range(nums):
        times = nums.count(nums[i])
        if times == 1:
            return nums[i]