class Solution:
    def finalString(s: str) -> str:
        stringList = list(s)
        for i in range(len(stringList) - 1, -1, -1):
            if stringList[i] == "i":
                stringList.pop(i)
        return "".join(stringList)

# Example usage
result = Solution.finalString("mississippi")
print(result)
