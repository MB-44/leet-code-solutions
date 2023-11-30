class Solution(object):
    def longestCommonPrefix(self,strs:list[str])->str:
        for i in range(len(strs[0])):
            if str[0][i] in [j for j in str[1:]]




if __name__ == "__main__":
    strs = ["flower","flight","flow"]
    