class Solution:
    def transpose(matrix: list[list[int]]) -> list[list[int]]:
        row = len(matrix)
        cols = len(matrix[0])
        result = [[0] * row for _ in range(cols)]
        for i in range(cols):
            for j in range(row):
                result[i][j] = matrix[i][j]
        return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
resultl = Solution.transpose(matrix)
print(resultl)