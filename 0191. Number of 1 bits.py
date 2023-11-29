class Solution:
    def hammingWeight(self,n:int)->int:
        count,binRe = 0, bin(n)[2:]
        for digit in binRe:
            if digit == "1":
                count += 1
        return count


if __name__ == "__main__":
    pass