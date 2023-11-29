class Solution:
    def sortByBits(arr):
        countD = {}
        binList = [bin(num)[2:] for num in arr]



if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8]
    result = Solution.sortByBits(arr)
    print(result)