class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nStr = str(n)
        output = int(nStr[0])

        for i in range(1,len(nStr)):
            if i%2!=0:
                x = int(nStr[i])
                output += -x
            else:
                output += int(nStr[i])
        return output