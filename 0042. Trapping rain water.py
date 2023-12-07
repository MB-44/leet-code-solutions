class Solution:
    def trap(height: list[int]) -> int:
        first, last = height[0], height[-1]
        total = 0
        for i in range(1,len(height)-1):
            if height[i] >height[i-1]:
                pass



if __name__ == "__main__":
    pass