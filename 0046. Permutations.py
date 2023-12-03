import random

c = [[1,3],[3,1]]
x = [1,3]
if random.shuffle(x) not in c:
    print(x)




# import random
# import math

# class Solution:
#     def permute(nums: list[int]) -> list[list[int]]:
#         count = math.factorial(len(nums))
#         newList = []
#         for i in range(count):
#             tempList = [nums[i]]
#             tempRemove = nums[:i]+ nums[i+1:]
#             c = 0
#             tempL = []

#             while c < count-1:
#                 random.shuffle(tempRemove)
#                 if tempRemove not in tempL:
#                     count += 1
#                     tempL.append(tempRemove.copy())

#             for i in range(len(tempL)):
#                 newList.append(tempList+tempL[i])

#         return newList

# if __name__ == "__main__":
#     nums = [1,2,3]
#     result = Solution.permute(nums)
#     print(result)
