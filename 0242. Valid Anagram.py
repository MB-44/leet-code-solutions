class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countDict = {}
        for char in t:
            char = char.lower()
            countDict[char] = countDict.get(char, 0) + 1
        for char in s:
            if char not in countDict or countDict[char] == 0:
                return False
            countDict[char] -= 1
        return all( value == 0 for value in countDict.values() )