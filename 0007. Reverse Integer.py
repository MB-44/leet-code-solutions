class Solution:
    def reverse(self, x: int):
        def signCheck(num):
            if num>0:
                return 1
            else: 
                return -1
        sign = signCheck(x)
        reverse = str(abs(x))[::-1]
        num = sign * int(reverse)

        if abs(num) > (2 ** 31 -1):
            return 0
        else: 
            return num


if __name__ == "__main__":
    pass