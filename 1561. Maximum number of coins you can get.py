class Solution(object):
    def maxCoins(self,pils):
        sortedPils = sorted(pils, reverse=True)
        maxCoins = 0
        n = len(pils)
        for i in range(n//3, n, 2):
            maxCoins += sortedPils[i]
        return maxCoins


if __name__ == "__main__":
    pils = [9,8,7,6,5,1,2,3,4]
    result = Solution().maxCoins(pils)
    print(result)