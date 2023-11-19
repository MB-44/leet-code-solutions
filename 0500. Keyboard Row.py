# To Do

class Solution(object):
    def findWords(self,words):
        keyBoard = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        output = words.copy()
        for row in keyBoard:
            for word in words:
                count = 0
                for letter in word:
                    if letter.lower() in row:
                        count += 1
                if len(word) == count:
                    output.append(word)
        return output

if __name__ == "__main__":
    words = ["Hello","Alaska","Dad","Peace"]
    print(Solution().findWords(words))
    