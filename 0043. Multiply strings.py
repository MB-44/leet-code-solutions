class Solution(object):
    def multiply(self,num1,num2):
        def func(stringInt):
            num = 0
            for ch in stringInt:
                if "0" <= ch <= "9":
                    num = num * 10 +(ord(ch) - ord("0"))
            return num
        return str(func(num1) * func(num2))

if __name__ == "__main__":
    num1,num2 = "2","3"
    x = Solution().multiply(num1,num2)
    print(x)