class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        indexZeros = []
        l01 = len(arr)
        
        for i in range(l01):
            if arr[i] == 0:
                indexZeros.append(i)
        
        cumulativeZeros = 0

        for i in range(l01):
            if i in indexZeros:
                arr.insert(i + cumulativeZeros, 0)
                cumulativeZeros += 1

        l02 = len(arr)
        diff = l02-l01
        
        while diff > 0:
            arr.pop()
            diff -= 1
