class Solution(object):
    def mergeAlternately(self, word1, word2):
        mergedStr, shortStrLen = "", len(word1)
        flag = False 
        if len(word1) != len(word2):
            flag = True
            if len(word1) > len(word2):
                shortStrLen = len(word2)
                extraStr = word1[len(word2):]
            else:
                shortStrLen = len(word1)
                extraStr = word2[len(word1):]
        for i in range(shortStrLen):
            mergedStr += word1[i] + word2[i]
        if flag:
            mergedStr += extraStr
            return mergedStr
        return mergedStr