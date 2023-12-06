class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        if len(pref) < 2:
            return pref        
        answer = [pref[0]]
        for i in range(1,len(pref)):
            answer.append(pref[i-1]^pref[i])
        return answer