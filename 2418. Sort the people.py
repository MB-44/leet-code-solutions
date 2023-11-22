class Solution(object):
    def sortPeople(self,names,heights):
        sortedPeople = []
        for height in sorted(heights, reverse=True):
            sortedPeople.append(names[heights.index(height)])
        return sortedPeople


if __name__ == "__main__":
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    result = Solution().sortPeople(names,heights)
    print(result)