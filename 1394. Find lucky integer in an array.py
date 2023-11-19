class Solution(object):
    def findLucky(self,arr):
        luckyNum = -1
        uniqueArr = list(set(arr))
        for num in uniqueArr:
            if arr.count(num) == num and luckyNum < num:
                luckyNum = num
        return luckyNum