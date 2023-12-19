def get_surrounding_indices(matrix, row, col):
    sumOfSurround = 0
    count = 0

    for i in range(max(0, row - 1), min(len(matrix), row + 2)):
        for j in range(max(0, col - 1), min(len(matrix[0]), col + 2)):
            sumOfSurround += matrix[i][j]
            count += 1
    
    return (sumOfSurround // count)

def print_surrounding_indices(matrix):
    outputMat = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            floorAvg = get_surrounding_indices(matrix, i, j)
            outputMat[i][j] = floorAvg

    return outputMat

# Example 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x = print_surrounding_indices(matrix)
print(x)