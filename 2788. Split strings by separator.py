class Solution(object):
    def splitWordsBySeparator(self,words,separator):
        returnStr = []
        for word in words:
            returnStr.extend(word.split(separator))
        while "" in returnStr:
            returnStr.remove("")
        return returnStr



if __name__ == "__main__":
    words = ["$easy$","$problem$"]
    separator = "$"
    result = Solution().splitWordsBySeparator(words,separator)
    print(result)
