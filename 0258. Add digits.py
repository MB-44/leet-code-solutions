class Solution:
    def addDigits(num: int) -> int:
        if len(str(num)) == 1:
            return num
        return Solution.addDigits(sum([int(digit) for digit in str(num)]))


if __name__ == "__main__":
    result = Solution.addDigits(38)
    print(result)