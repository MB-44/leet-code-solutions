class Solution:
    def containsDuplicate(nums):
        return not (len(nums) == len(set(nums)))

#477ms
if __name__ == "__main__":
    nums = [1,2,3,4]
    result = Solution.containsDuplicate(nums)
    print(result)