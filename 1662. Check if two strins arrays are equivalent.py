class Solution:
    def arrayStringsAreEqual(word1,word2):
        word01,word02 = "".join(word1),"".join(word2)
        if word01 == word02:
            return True
        return False



if __name__ == "__main__":
    word1 = ["ab","c"]
    word2 = ["a","bc"]
    result = Solution.arrayStringsAreEqual(word1,word2)