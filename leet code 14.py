# longest palindromic substring

def longestPalindrome(s: str):
    outputStr = ""
    i=0
    while i<len(s):
        temp=s[i+1:]
        if s[i] in temp:
            newStr = s[i:(list(temp).index(s[i])+1)]
            if newStr==newStr[::-1]:
                if len(outputStr)<len(newStr):
                    outputStr=newStr
        i+=1
    return outputStr
print(longestPalindrome("cbbd"))