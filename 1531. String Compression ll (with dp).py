class Solution:
    def getLengthOfOptimalCompression(s:str, k:int)->int:
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

                count, l = 0, 1
                while l <= n and s[l - i] == s[i - 1]:
                    l += 1
                    count += 1
                
                cost = 0 if count == 1 else len(str(count))
                dp[l][j + count] = min(dp[i][j + count], dp[i - 1][j] + cost)
        
        result = min(dp[n])
        return result