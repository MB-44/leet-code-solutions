class Solution:
    def removeAlmostEqualCharacters(self,word:str)->int:
        n = len(word)
        operations = 0

        i = 0
        while i < n - 1:
            if word[i] == word[i + 1]:
                operations += 1
            i += 2  # Move two positions ahead to skip the adjacent pair
        else:
            i += 1  # Move to the next character

        return operations   

word = "abcd"
result = Solution.removeAlmostEqualCharacters(word)
print(result)