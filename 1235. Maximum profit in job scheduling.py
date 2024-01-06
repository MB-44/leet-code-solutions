from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        number_of_jobs = len(profit)

        dp = [0] * (number_of_jobs + 1)

        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)
        
        return dp[number_of_jobs]