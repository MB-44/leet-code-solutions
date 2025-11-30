class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters.append(target)
        letters = sorted((list(set(letters))))
        if letters.index(target) == -1:
            return letters[0]
        return letters[letters.index(target)+1]