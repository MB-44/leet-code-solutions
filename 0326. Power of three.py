class Solution:
    def isPowerOfThree(n:int)->bool:
        if n == 1:
            return True
        elif n < 1 or n%3 != 0:
            return False
        return Solution().isPowerOfThree(n/3)


if __name__ == "__main__":
    print(pow())