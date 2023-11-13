# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str):
        uniqueStr1  = ""
        for i in (list(set(s))):
            uniqueStr1 += i
        #return uniqueStr1
        if len(uniqueStr1) == len(s):
            return False
        else: 
            if s.count(uniqueStr1):
                return True
            return False

examp1 = Solution().repeatedSubstringPattern("abab")
print(examp1)