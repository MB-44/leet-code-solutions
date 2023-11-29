class Solution:
    def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
        if (purchaseAmount/5)%2 == 1:
            roundNum = purchaseAmount + 5
        else: 
            roundNum = round(purchaseAmount,-1)
        return 100-roundNum

if __name__ == "__main__":
    pa = 5
    result = Solution.accountBalanceAfterPurchase(pa)
    print(result)