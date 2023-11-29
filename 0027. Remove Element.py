class Solution(object):
    def removeElement(self,nums:list[int],val:int)->int:
        k = 0
        for num in nums:
            if num == val:
                num.remove(num)
                continue
            


if __name__ == "__main__":
    pass