class Solution(object):
    def addToArrayForm(self, num, k):
        number = int("".join([str(n) for n in num])) + k
        return [int(i) for i in str(number)]
        
if __name__ == "__main__":
    nums = [1,2,0,0] 
    k = 34
    result = Solution().addToArrayForm(nums,k)
    print(result)