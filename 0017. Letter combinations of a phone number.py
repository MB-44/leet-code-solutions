class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {
            "2":"abc",  "3":"def",  "4":"ghi",
            "5":"jkl",  "6":"mno",  "7":"pqrs",
            "8":"tuv",  "9":"wxyz"  }
        
        lis = []