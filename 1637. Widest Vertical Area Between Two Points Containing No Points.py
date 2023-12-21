class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        maxWidth = 0
        for i in range(1,len(points)):
            currentWidth = points[i][0] - points[i-1][0]
            maxWidth = max(maxWidth,currentWidth)

        return maxWidth        