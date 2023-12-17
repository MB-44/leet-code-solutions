class Solution:
    def checkRecord(s: str) -> bool:
        return list(s).count("A") < 2 or list(s).count("L") < 3
        