class Solution(object):
    def searchInsert(self,num,target):
        if target in num:
            return num.index(target)
        elif max(num) < target:
            return len(num)
        elif target < min(num):
            return 0
        for i in range(len(num)-1):
            if target > num[i] and target < num[i+1]:
                return i+1



if __name__ == "__main__":
    nums = [1,3,5,6]
    x = Solution().searchInsert(nums,2)
    print(x)