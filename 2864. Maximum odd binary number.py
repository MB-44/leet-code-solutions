# This will exceed the time limit
class Solution(object):
    def maximumOddBinaryNumber(self,s:str)->str:
        length, countOne = len(s.strip()), list(s).count("1")
        maxVal = (2**length)-1
        while maxVal != 0:
            if maxVal % 2 == 1 and list(bin(maxVal)[2:]).count("1")==countOne:
                return bin(maxVal)[2:].zfill(length)
            maxVal -= 1

# This one too
class Solution:
    def maximumOddBinaryNumber(s):
        length, countOne = len(s.strip()), list(s).count("1")
        maxVal = int("1"*length,2)
        while maxVal > 0:
            if maxVal%2 == 1 and bin(maxVal).count("1") == countOne:
                return bin(maxVal)[2:].zfill(length)
            maxVal -= 1
        return None

# Oh my god, this is too easy, just now figured out
def maximumOddBinaryNumber(s):
    countOne = s.count("1")
    return "1" * (countOne-1) + "0" * (len(s) - countOne) + "1"



if __name__ == "__main__":
    s = "01000100011100011000000000010100100001"
    result = Solution.maximumOddBinaryNumber(s)
    print(result)

"""
1 --> 1
2 --> 3
3 --> 7
4 --> 15


"""