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
            
if __name__ == "__main__":
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    result = Solution.findContentChildren(g,s)
    print(result)