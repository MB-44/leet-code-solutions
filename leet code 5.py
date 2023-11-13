def pivotIndex1(nums):
   leftSum, rightSum = 0,sum(nums)
   for index in range(len(nums)):
       rightSum -= nums[index]
       if leftSum==rightSum:
           return index
       leftSum += nums[index]
   return -1

def pivotIndex2(nums):  
        nums = [0] + nums + [0]
        left, right = 0, sum(nums[2:])
        for index in range(1,len(nums)-1):
            if left==right: 
                return  index-1
            left += nums[index]
            right -= nums[index+1]
        return -1

def pivotIndex3(nums: list):
    if not(nums) or len(nums)<3:
        return -1
    rightSum, leftSum = sum(nums), 0
    for index in range(len(nums)):
        rightSum -= nums[index]
        if rightSum == leftSum:
            return index
        leftSum += nums[index]







