class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        goodOnes = 0
        if len(startTime) == 1:
            if queryTime in range(startTime[0],endTime[0]+1):
                return 1
        
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                goodOnes += 1
        return goodOnes
            
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                res += 1 