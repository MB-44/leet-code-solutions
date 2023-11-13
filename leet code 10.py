def search(nums: list[int], target: int):
    for num in nums:
        if target==num:
            return nums.index(num)
            break
    else: 
        return -1
print(search([1,2,3,3,5],4))