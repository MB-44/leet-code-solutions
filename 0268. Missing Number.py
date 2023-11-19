# 1343ms

def missingNumber(nums):
    for num in range(0,max(nums)+1):
        if num not in nums:
            return num
    return max(nums)+1