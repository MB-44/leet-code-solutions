class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            max01 = max(stones)
            stones.remove(max01)
            max02 = max(stones)
            if max01 == max02:
                continue
            newStone = max01 - max02
            stones.append*newStone
        return stones[0]




if __name__ == "__main__":
    pass
        