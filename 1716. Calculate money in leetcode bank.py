class Solution:
    def totalMoney(n: int) -> int:
        # return n%7 , n//7
        total = 0
        for i in range(n//7):
            for j in range(7):
                total += j + i + 1
        for k in range(i+1,(n%7)+2):
            total += k +1
        return total

if __name__ == "__main__":
    n = 20
    result = Solution.totalMoney(n)
    print(result)

# 1, 2, 3, 4, 5, 6, 7