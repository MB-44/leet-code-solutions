class Solution(object):
    def longestCommonPrefix(strs:list[str])->str:
        
        if not strs:
            return ""

        minLenStr = min(strs, key=len)
        returnStr = ""

        for s in minLenStr:
            flag = True
            for k in strs:
                if not k.startswith(s):
                    flag = False
                    break
                elif  (minLenStr.index(s) != k.index(s)):
                    flag = False
                    break
            if flag:
                returnStr += s
        return returnStr

if __name__ == "__main__":
    strs = ["flower","flight","flow"]
    result = Solution.longestCommonPrefix(strs)
    print(result)