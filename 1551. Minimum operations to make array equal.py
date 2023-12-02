class Solution:
    def minOperations(n: int) -> int:
        return (n*n) // 4

# [1,3,5,7,9,11]
# [1,3,5,7,9]
# n-1

# [1,3,5]
# [2,4,8]
# n-1

# s = (first_element + last element (n-1)) / (n // 2)