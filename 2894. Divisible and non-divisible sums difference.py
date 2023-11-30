class Solution:
    def differenceOfSums(n,m):
        num1 = sum([i for i in range(1,n+1) if i%m!=0])
        num2 = sum([i for i in range(1,n+1) if i%m==0])
        return num1 - num2

if __name__ == "__main__":
    result = Solution.differenceOfSums(10,2)
    print(result)