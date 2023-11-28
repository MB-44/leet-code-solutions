class Solution:
    def maxArea(self,heigh:list[int])->int:
        n = len(heigh)
        maxArea = 0
        for i in range(n):
            for j in range(i,n):
                temp = heigh[i]*heigh[j]
                if temp > maxArea:
                    l = [i,j]
                    maxArea = temp
        return [maxArea,l]

if __name__ == "__main__":
    h = [1,8,6,2,5,4,8,3,7]
    result = Solution().maxArea(h)
    print(result)