class Solution:
    def halvesAreAlike(s: str) -> bool:
        mid = len(s)//2
        a, b = s[:mid], s[mid:]
        countA = [letter for letter in a if letter.lower() in "aeiou"]
        countB = [letter for letter in b if letter.lower() in "aeiou"]
        return len(countA) == len(countB)


if __name__ == "__main__":
    s = "book"
    result = Solution.halvesAreAlike(s)
    print(result)