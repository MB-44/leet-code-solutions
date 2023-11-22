class Solution(object):
    def countWords(self,words1,words2):
        count = 0
        for word in words1:
            if word in words2 and (words1.count(word)+words2.count(word))==2:
                count += 1
        return count

if __name__ == "__main__":
    words1 = ["leetcode","is","amazing","as","is"]
    words2 = ["amazing","leetcode","is"]
    result = Solution().countWords(words1,words2)
    print(result)