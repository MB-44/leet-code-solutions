class Solution:
    def numberOfMatches(self,n: int) -> int:
        numOfMatches = 0
        while n > 1:
            if n%2!=0:
                numOfMatches += int(n/2)
                n = ((n-1)/2) + 1
            else: 
                numOfMatches += n//2 
                n //= 2
        return int(numOfMatches)