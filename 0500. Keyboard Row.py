class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        firstRow = {"q","w","e","r","t","y","u","i","o","p"}
        secondRow = {"a","s","d","f","g","h","j","k","l"}
        thirdRow = {"z","x","c","v","b","n","m"}

        keyboard = [
            {"q","w","e","r","t","y","u","i","o","p"},
            {"a","s","d","f","g","h","j","k","l"},
            {"z","x","c","v","b","n","m"}
        ]

        outputArray = []

        for word in words:
            wordSet = set(word.lower())
            for letter in wordSet:
                pass