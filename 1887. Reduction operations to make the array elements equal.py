# Time limit exceeded
def reductionOperations(nums):
    count = 0
    if len(set(nums)) == 1:
        return count
    while len(set(nums)) > 1:
        indexOfLargest = nums.index(max(nums))
        indexOfnextLargest = nums.index(
            max([i for i in nums if i<nums[indexOfLargest]]))
        nums[indexOfLargest] = nums[indexOfnextLargest]
        count += 1
    return count


# 751ms
def reductionOperations(nums):
    count = 0
    sorted_nums = sorted(nums, reverse=True)
    
    for i in range(len(nums) - 1):
        if sorted_nums[i] > sorted_nums[i + 1]:
            count += i + 1

    return count


x = reductionOperations([5,1,3])
print(x)

        
        
