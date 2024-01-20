class Solution:
    def minimumCost(nums: list[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        minArray = []
        minIndex = []
        minSum = 0
        
        for _ in range(3):
            minEach = min(nums)
            index = nums.index(minEach)
            minIndex.append(index)
            minArray.append(minEach)
            nums.pop(index)
        
        # for i in range(3):
        #     nums.insert(minIndex[i], minArray[i])
        
        return sum(minArray)



if __name__ == "__main__":
    input = [1,2,3]
    output = Solution.minimumCost(input)
    print(output)