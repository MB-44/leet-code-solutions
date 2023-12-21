class Solution:
    def buyChoco(prices, money):
        prices.sort()
        toBuy = prices[0] + prices[1]
        if toBuy > money:
            return money
        return (money - toBuy) 
    

if __name__ == "__main__":
    prices = [3,1,2,2]
    money = 3
    result = Solution.buyChoco(prices, money)
    print(result)