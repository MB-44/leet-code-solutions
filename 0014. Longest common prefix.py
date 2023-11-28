class Solution(object):
    def longestCommonPrefix(self,strs:list[str])->str:
        for i in strs:
            for j in i:
                if j in [k for k in strs]


if __name__ == "__main__":
    strs = ["flower","flight","flow"]
    print(set(strs[0]))