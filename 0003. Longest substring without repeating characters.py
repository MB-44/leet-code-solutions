class Solution(object):
    def lengthOfLongestSubstring(self,s):
        substring = ""
        if len(set(s)) == 1:
            return 1
        for i in range(len(s)):
            for j in range(len(s)-1,-1,-1):
                if s[i]==s[j]:
                    substring = s[i:j+1]
        return substring

if __name__ == "__main__":
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)