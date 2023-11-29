class Solution:
    def canBeEqual(s1,s2):
        flag = True
        for i in range(4):
            for j in range(4):
                if (i-j)==2:
                    s1[i],s2[j] = s2[j],s1[i]
                    if s1 != s2:
                        flag = False
        return flag

if __name__ == "__main__":
    s1,s2 = "abcd","dacb"
    result = Solution.canBeEqual(s1,s2)
    print(result)