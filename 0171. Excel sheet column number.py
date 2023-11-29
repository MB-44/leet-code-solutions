class Solution:
    def titleToNumber(self,columnTitle:str)->int:
        if len(columnTitle) == 1:
            return ord(columnTitle) - ord('A')+1
        
        titleNum,count = 0,len(columnTitle)
        
        for letter in columnTitle[::-1]:
            titleNum = titleNum +  ((26**count-1) * ord(letter)%64)
            count -= 1
        
        return titleNum


if __name__ == "__main__":
    title = "ZY"
    result = Solution().titleToNumber(title)
    print(result)