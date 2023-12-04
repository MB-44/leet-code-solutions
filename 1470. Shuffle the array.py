class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        part1, part2 = nums[:n], nums[n:]
        output = []
        for p1, p2 in zip(part1,part2):
            output.append(p1,p2)
        return output