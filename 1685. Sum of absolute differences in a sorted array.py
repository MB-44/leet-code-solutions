# class Solution(object):
#     def getSumAbsoluteDifferences(self, nums):
#         output = [0]*len(nums)
#         for i in range(len(nums)):
#             eachSum = 0
#             for j in range(len(nums)):
#                 eachSum += abs(nums[i]-nums[j])
#             output[i] = eachSum
#         return output

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)

        # Calculate the cumulative sum from the left
        left_sum = [0] * n
        left_sum[0] = nums[0]
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i]

        # Calculate the cumulative sum from the right
        right_sum = [0] * n
        right_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i]

        # Calculate the result using cumulative sums
        output = [0] * n
        for i in range(n):
            left_diff = i * nums[i] - left_sum[i]
            right_diff = right_sum[i] - (n - 1 - i) * nums[i]
            output[i] = left_diff + right_diff

        return output

# Example usage
nums = [2, 3, 5]
solution = Solution()
result = solution.getSumAbsoluteDifferences(nums)
print(result)



