class Solution(object):
    def createTargetArray(nums,index):
        targetArr = ["_"]*len(nums)
        for i in range(len(targetArr)):
            targetArr.insert(index[i],nums[index[i]])
        return targetArr

if __name__ == "__main__":
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    result = Solution.createTargetArray(nums,index)
    print(result)