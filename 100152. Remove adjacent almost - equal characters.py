class Solution:
    def removeAlmostEqualCharacters(self,word:str)->int:
        if len(set(list(word))) == len(list(word)):
            return 0
        count = []
        for char in list(set(list(word))):
            count.append(list(word).count(char))
        return count

word = "abcd"
result = Solution.removeAlmostEqualCharacters(word)
print(result)