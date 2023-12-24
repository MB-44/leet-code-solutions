class Solution:
    def minOperations(s: str) -> int:
        subStr = [s[i: i+2] for i in range(0,len(s),2)]
        unique = list(set(subStr))



s = "10100"
l = 2

substr = [s[i : i+l] for i in range(0, len(s), l)]

print(substr)