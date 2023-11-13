class Solution():
    def isAnagram(self,s:str,t:str):
        if len(s) == len(t):
            tCopy = ""
            for i in range(len(s)):
                if s[i] in t:
                    tCopy += s[i]
                    index = t.index(s[i])
                    t = t[:index] + t[index+1:]
            if len(tCopy) == len(s):
                return True
            return False
        else: 
            return False

exp1 = Solution().isAnagram("aacc","ccac")
print(exp1)