class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0) == (divisor > 0):
            sign = 1
        else: 
            sign = -1
        
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        
        return max(min(quotient*sign,2**31-1),-2**31-1)