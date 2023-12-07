class Solution:
    def largestOddNumber(num: str) -> str:
        # for digit in num[::-1]:
        #     if int(digit) % 2 == 1:
        #         return num[:num.index(digit)+1]
        # return ""

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""

if __name__ == "__main__":
    num = "10133890"
    result = Solution.largestOddNumber(num)
    print(result)