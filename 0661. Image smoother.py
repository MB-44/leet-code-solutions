class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:

        def get_surrounding_indices(matrix, row, col):
            sumOfSurround = 0
            count = 0

            for i in range(max(0, row - 1), min(len(matrix), row + 2)):
                for j in range(max(0, col - 1), min(len(matrix[0]), col + 2)):
                    sumOfSurround += matrix[i][j]
                    count += 1
    
            return (sumOfSurround // count)
        
        rows = len(img)
        cols = len(img[0])

        outputMat = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                floorAvg = get_surrounding_indices(img, i, j)
                outputMat[i][j] = floorAvg

        return outputMat