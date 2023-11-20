class Solution(object):
    def isPowerOfFour(self,n):
        if n>0 and (n & (n-1) ==0) and (n%3==1):
            return True
        return False 


if __name__ == "__main__":
    num = 8
    output = Solution().isPowerOfFour(num)
    print(output)