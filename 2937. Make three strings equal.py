class Solution:
    def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
        prefix = ""
        for letter in s1:
            for s in [s2,s3]:
                if letter in s2 and letter in s3:
                    prefix += letter
        prefix = list(set(prefix))
        prefix.sort()
        return prefix

s1 = "dac"
s2 = "bac"
s3 = "cac"
result = Solution.findMinimumOperations(s1,s2,s3)
print(result)