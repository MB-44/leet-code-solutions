class Solution:
    def addStrings(num1,num2):
        n1 = n2 = 0
        for chr in num1:
            if "0" <= chr <= "9":
                n1 = n1 * 10 + (ord(chr)-ord("0"))
                continue
            break

        for chr in num2:
            if "0" <= chr <= "9":
                n2 = n2 * 10 + (ord(chr)-ord("0"))
                continue
            break
        return str(n1+n2)


if __name__ == "__main__":
    pass