class Solution:
    def maxProfit(self, prices: list[int]):
            maxProfit,minProfit = 0,prices[0]
            for index in range(1,len(prices)):
                if prices[index] < minProfit:
                    minProfit=prices[index]
                if maxProfit < prices[index]-minProfit:
                    maxProfit = prices[index]-minProfit
            return maxProfit

# prices is linked list, 
# if you want to run this in vscode you hv to create a linkedlist called prices