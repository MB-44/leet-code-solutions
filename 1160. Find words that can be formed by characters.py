class Solution:
    def countCharacters(words: list[str], chars: str) -> int:
        output = 0
        for word in words:
            canForm = True
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    canForm = False
                    break
            if canForm:
                output += len(word)
        return output

if __name__ == "__main__":
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    result = Solution.countCharacters(words,chars)
    print(result)