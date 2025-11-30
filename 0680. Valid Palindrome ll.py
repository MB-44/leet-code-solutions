class Solution(object):
    def validPalindrome(self, s):
        listedS = list(s)
        
        if self.isPalindrome(listedS):
            return True
        
        for i in range(len(listedS)):
            temp = listedS[:i] + listedS[i+1:]
            if self.isPalindrome(temp):
                return True
        return False

        def isPalindrome(self, arr):
            left, right = 0, len(arr) - 1
            while left < right:
                if arr[left] != arr[right]:
                    return False
                left += 1
                right -= 1
            return True