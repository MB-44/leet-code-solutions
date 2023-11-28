class Solution:
    def titleToNumber(self,columnTitle:str)->int:
        if len(columnTitle) == 1:
            return ord(columnTitle)%64
        titleNum,count,i = 0,0,len(columnTitle)
        for letter in columnTitle[::-1]:
            titleNum += ord(letter)%64
            count = 26
            i-=1
            if i!=0:
                titleNum+=count
        return titleNum

if __name__ == "__main__":
    title = "ZY"
    result = Solution().titleToNumber(title)
    print(result)