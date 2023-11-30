class Solution:
    def differenceOfSum(nums):
        sumOfNums = sum(nums)
        sumOfDigits = sum(int(digit) for i in nums for digit in str(i))
        return abs(sumOfNums-sumOfDigits)

if __name__ == "__main__":
    nums = [1,15,6,3]
    result = Solution.differenceOfSum(nums)
    print(result)
