# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self,haystack:str,needle:str):
        if needle in haystack:
            i = haystack.index('needle')
            return i
        else:
            return -1
        
def strStr(haystack:str,needle:str):
    if needle in haystack:
        i = haystack.index('needle')
        return i
    else:
        return -1
    
k = strStr("sadbutsad","sad")
print(k)