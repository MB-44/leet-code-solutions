class Solution(object):
    def isMonotonic(self, nums):
        if len(list(set(nums))) != 1:
            increase, decrease = True, True
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    increase = False
                if nums[i] > nums[i-1]:
                    decrease = False
            if decrease or increase:
                return True
            return False
        return True        


# To Check if it's an increasing array
# array = [1,2,3,4,3,4,6,7]
# increase = True
# for i in range(1,len(array)):
#     if array[i] < array[i-1]:
#         increase = False
#         break
# print(increase)

# To check if it's a decreasing array
# array = [6,5,4,3,2,1]
# decrease = True
# for i in range(1,len(array)):
#     if array[i] > array[i-1]:
#         decrease = False
#         break
# print(decrease)