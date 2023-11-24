class Solution(object):
    def reverseVowels(self,s):
        vowels = "aeiou"
        s = list(s)
        vowelsInS = ""
        for letter in s:
            if letter.lower() in vowels:
                vowelsInS += letter
        count = 0
        vowelsInS = vowelsInS[::-1]
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = vowelsInS[count]
                count += 1
        return "".join(s)

if __name__ == "__main__":
    s = "hello"
    result = Solution().reverseVowels(s)
    print(result)