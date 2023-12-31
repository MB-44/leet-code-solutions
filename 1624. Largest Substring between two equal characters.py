class Solution:
    def maxLengthBetweenEqualCharacters(s: str) -> int:
        ans = -1
        length = len(s)

        for left in range(length):
            for right in range(left + 1, length):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)
        return ans