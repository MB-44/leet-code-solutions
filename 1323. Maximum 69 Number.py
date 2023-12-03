class Solution:
    def maximum69Number (num: int) -> int:
        sNum = list(str(num))
        maxNum = num
        s = sNum
        for i in range(len(sNum)):
            if s[i] == "6": s[i] = "9"
            else: s[i] = "6"
            temp = int("".join(s))
            if temp > maxNum: maxNum = temp
            if sNum[i] == "6": s[i] = "9"
            else: sNum[i] = "6"
        return maxNum