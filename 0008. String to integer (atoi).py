class Solution(object):
    def myAtoi(self,s):
        s = s.strip()
        if not s or (len(s)==1 or not(s.isdigit())):
            return 0
        integer, op = "", 1
        for i in s:
            if i in "-" and s[s.index(i)+1].isdigit():
                op = -1
                continue
            if i.isdigit():
                integer += i
            else: 
                break
        if not integer:
            return 0
        integer = int(integer)
        if op == -1:
            integer = integer*op
        return max(min(integer,2**31-1),-2**31)

if __name__ == "__main__":
    s = "-"
    result = Solution().myAtoi(s)