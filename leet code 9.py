def maxProfit(prices: list[int]) -> int:
    maxProfit,minProfit = 0,prices[0]
    for index in range(1,len(prices)):
        if prices[index] < minProfit:
            minProfit=prices[index]
        if maxProfit < prices[index]-minProfit:
            maxProfit = prices[index]-minProfit
    return maxProfit

print(maxProfit([7,6,4,3,1]))

# maxProfit=0
#     for num1 in prices:
#         for num2 in prices[prices.index(num1):]:
#             maxProfit = max(maxProfit,num2-num1)                
#     return maxProfit
