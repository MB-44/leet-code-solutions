class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        dic = {
            "2":"abc",  "3":"def",  "4":"ghi",
            "5":"jkl",  "6":"mno",  "7":"pqrs",
            "8":"tuv",  "9":"wxyz"  }
        
        lis = []
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                lis.append(curStr)
                return
        
        