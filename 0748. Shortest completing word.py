class Solution(object):
    def shortestCompletingWord(self,licensePlate,words):
        countLetters = {}
        for i in licensePlate.upper():
            if i.strip() != "":
                try:
                    int(i)
                except ValueError:
                    countLetters[i] = licensePlate.upper().count(i)
        wordIndex = 0
        for word in words[::-1]:
            for letter in word.upper():
                if countLetters[letter] == list(word).count(letter):
                    return words.index(word)


if __name__ == "__main__":
    lp = "1s3 456"
    words = ["looks","pest","stew","show"]
    result = Solution().shortestCompletingWord(lp,words)
    print(result)