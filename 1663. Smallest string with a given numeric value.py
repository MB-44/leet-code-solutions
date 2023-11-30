class Solution:
    def getSmallestString(n,k):
        if n==1 and k  < 27:
            return chr(k+96)
        result = ['a']*n
        for i in range(n):
            if k > 26:
                result[i] = chr((k%26)+96)
                k //= 26
            else: 
                result[i] = chr(k+96)
                break
        
        return "".join(result)
        



if __name__ == "__main__":
    n,k = 3,27
    result = Solution.getSmallestString(n,k)
    print(result)