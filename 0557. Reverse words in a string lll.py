class Solution(object):
    def reverseWords(self,s):
        reversedList = []
        for word in s.split(" "):
            reversedList.append(word[::-1])
        return " ".join(reversedList)


# class Solution(object):
#     def reverseWords(self, s):
#         return " ".join([i[::-1] for i in s.split()])
        

if __name__ == "__main__":
    s = "Let's take Leetcode contest"
    x = Solution().reverseWords(s)
    print(x)