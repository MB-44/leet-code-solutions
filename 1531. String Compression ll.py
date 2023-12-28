class Solution:
    def getLengthOfOptimalCompression(s: str, k: int) -> int:
        numOfLetter = {}
        l = list(set(s))
        l.sort()
        for letter in l:
            numOfLetter[letter] = s.count(letter)
        
        for _ in range(k):
            minLetter = min(numOfLetter, key=numOfLetter.get)
            minCount = numOfLetter[minLetter]
            
            if minCount > 0:
                numOfLetter[minLetter] -= 1
            
            if numOfLetter[minLetter] == 0:
                del numOfLetter[minLetter]
        
        # print(numOfLetter)
        ans = ""
        for letter in numOfLetter:
            if numOfLetter[letter] > 1:
                ans += (letter + str(numOfLetter[letter]))
            else: 
                ans += letter
        print(len(ans))

if __name__ == "__main__":
    s, k = "abc", 2
    result = Solution.getLengthOfOptimalCompression(s,k)
    print(result)