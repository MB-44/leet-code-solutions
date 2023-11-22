class Solution(object):
    def maximumNumberOfStringPairs(self,words):
        count = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if words[i] == words[j][::-1] and i < j:
                    count += 1
        return count

if __name__ == "__main__":
    words = ["cd","ac","dc","ca","zz"]
    result = Solution().maximumNumberOfStringPairs(words)
    print(result)