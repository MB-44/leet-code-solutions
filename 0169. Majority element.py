class Solution:
    def majorityElement(self,nums:list[int])->int:
        candidate, count = None, 0

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else: 
                count -= 1
        countCandidate = nums.count(candidate)
        return candidate if countCandidate > len(nums)/2 else -1
if __name__ == "__main__":
    s = [2,2,1,1,1,2,2]
    # count = 2