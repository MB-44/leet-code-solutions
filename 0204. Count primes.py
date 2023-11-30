class Solution:
    def countPrimes(n: int) -> int:
        def isPrime(num):
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return False
                continue
            return True
        
        if n <= 2:
            return 0
        count = 0

        for i in range(2,n):
            if isPrime(i):
                count += 1
        return count
    
    
num = 10
result = Solution.countPrimes(num)
print(result)