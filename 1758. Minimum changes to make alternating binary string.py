class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count_if_start_0 = 0
        count_if_start_1 = 0

        for i in range(0,n):
            if i%2==0:
                if s[i] == '1':
                    count_if_start_0 += 1
                else:
                    count_if_start_1 += 1
            else:
                if s[i] == '0':
                    count_if_start_0 += 1
                else:
                    count_if_start_1 += 1
        

        return min(count_if_start_0,count_if_start_1)
 
        