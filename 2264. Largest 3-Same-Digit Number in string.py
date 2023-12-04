class Solution:
    def largestGoodInteger(self,num: str) -> str:
        output = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                output = max(output, int(num[i]))
        if output == -1:
            return ""
        return str(output)*3