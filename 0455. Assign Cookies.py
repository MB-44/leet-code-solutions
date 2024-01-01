# to be continued
# class Solution:
#     def findContentChildren(g: list[int], s: list[int]) -> int:
#         gLen = len(g)
#         count = 0
#         for i in range(gLen):
#             if i > len(s)-1:
#                 break
#             elif s[i] >= g[i]:
#                 count += 1
#                 continue
#         return count
            

class Solution:
    def findContentChildren(g: list[int], s: list[int]) -> int:
        ans = 0
        i, j = 0, 0
        
        s.sort(reverse=True)
        g.sort(reverse=True)

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                i += 1
        
        return ans

if __name__ == "__main__":
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    result = Solution.findContentChildren(g,s)
    print(result)