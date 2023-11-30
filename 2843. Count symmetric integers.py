class Solution:
    def countSymmetricIntegers(low,high):
        if len(str(high)) % 2 == 1:
            high -= 1
        digits = max(len(str(low)),len(str(high)))
        count = 0
        half = int(digits)//2
        for i in range(low,high+1):
            leftSum = sum([int(digit) for digit in str(i)[:half+1]])
            rightSum = sum([int(digit) for digit in str(i)[-1:half-1:-1]])
            if leftSum == rightSum:
                count += 1
        return count

result = Solution.countSymmetricIntegers(1,100)
print(result)