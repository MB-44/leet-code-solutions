def runningSum(nums: list[int]):
    returnList = [sum(nums)]
    temp=0;
    for num in nums[-1:0:-1]:
        temp += num 
        returnList.insert(0,sum(nums)-temp)
    return returnList
    
print(runningSum([1,2,3,4]))