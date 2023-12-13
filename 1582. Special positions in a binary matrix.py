class Solution:
    def numSpecial(mat: list[list[int]]) -> int:
        indexs = []
        row,itemCount = 0,0
        flattendMat = [item for row in mat for item in row]
        for item in flattendMat:
            if itemCount == 3:
                itemCount = 0
                row += 1
            if item == 1:
                indexs.append([row,itemCount])
            itemCount += 1
        
        for index in indexs:
            if indexs:
                pass


if __name__ == "__main__":
    mat = [[1,0,0],[0,0,1],[1,0,0]]
    result = Solution.numSpecial(mat)
    print(result)
        