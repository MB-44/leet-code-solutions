class Solution(object):
    def convertToTitle(self,columnNumber:int)->str:
        s = ""
        while 0 < columnNumber:
            s = chr(ord('A')+(columnNumber-1)%26) + s
            columnNumber = (columnNumber-1)//26
        return s

if __name__ == "__main__":
    colNUm = 27

# ord() -> this func takes a character as an argument and returns the unicode
# example:- print(ord('A')) -> output -> 65

# chr() -> this func take a int representing a unicode code point 
# returns the corresponding character
# example:- print(chr(65)) -> output -> "A"