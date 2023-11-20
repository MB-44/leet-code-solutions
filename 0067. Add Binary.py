class Solution(object):
    def addBinary(self, a:str, b:str):
        addedBin = bin(int(a,2) + int(b,2))
        return str(addedBin[2:])


if __name__ == "__main__":
    a, b = "11","1"
    x = Solution().addBinary(a,b)
    print(x)