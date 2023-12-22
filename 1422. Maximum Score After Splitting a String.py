class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        for i in range(1,len(s)):
            leftSubCount = s[:i].count("0")
            rightSubCount = s[i:].count("1")
            maxScore = max(maxScore, (rightSubCount + leftSubCount))
        return maxScore

# s = "01110"
# Solution.maxScore(s)
# result = Solution.maxScore(s)
# print(result)