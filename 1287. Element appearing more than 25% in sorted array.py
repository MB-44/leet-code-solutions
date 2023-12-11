class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        size = len(arr)
        quater = size // 4 
        count = 1
        position = arr[0]

        for i in range(1,size):
            if position == arr[i]:
                count += 1
            else:
                count = 1
            
            if count > quater:
                return arr[i]
            position = arr[i]
            
        return position