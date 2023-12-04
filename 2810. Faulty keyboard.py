class Solution:
    def finalString(s: str) -> str:
        strList = list(s)
        l = []
        for i in range(len(strList)):
            if strList[i] == "i":
                l = strList[:i][::-1]
            else: 
                l.append(strList[i])
        countI = l.count("i")
        for i in range(countI):
            l.remove("i")
        return "".join(l)

# Example usage
result = Solution.finalString("mississippi")
print(result)
