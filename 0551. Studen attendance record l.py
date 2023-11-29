class Solution:
    def checkRecord(self,s):
        return list(s).count("A") < 2 or list(s).count("L") < 3