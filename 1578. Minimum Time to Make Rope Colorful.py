class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        mx = total = neededTime[0]
        ans = 0
        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                mx = max(mx, neededTime[i])
                total += neededTime[i]
            else:
                ans += (total-mx)
                total = mx = neededTime[i]
        return ans + (total - mx)