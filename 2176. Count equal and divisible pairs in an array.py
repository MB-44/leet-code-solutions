class Solution:
    def countPairs(nums: list[int], k: int) -> int:
        numOfPairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    numOfPairs += 1
        return numOfPairs



if __name__ == "__main__":
    nums = [3,1,2,2,2,1,3]
    k = 2
    result = Solution.countPairs(nums,k)
    print(result)
