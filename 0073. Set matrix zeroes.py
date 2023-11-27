# Solution 01 - this will not help for you, i'm working on it
class Solution(object):
    def setZeroes(self, matrix):
        indexs = [] 
        for list in matrix:
            if 0 in list:
                indexs.append([matrix.index(list),list.index(0)])
        
        for i in range(len(matrix)):
            if i in [row[0] for row in indexs]:
                matrix[i] = [0]*len(matrix[i])
                continue
        for j in range(len(matrix[i])):
            if j in [row[1] for row in indexs]:
                for k in range(len(matrix)):
                    if len(matrix[i]) > j:
                        matrix[k][j] = [0]*len(matrix)
        return matrix


# Solution 02 - this will work
# seroRows mean 0Rows, you know the missing letter, 
# it's not working in my keyboard, f*** letter
class Solution(object):
    def setZeroes(self,matrix):
        rows, cols = len(matrix), len(matrix[0])
        seroRows, seroCols = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    seroCols.add(j)
                    seroRows.add(i)
        
        for row in seroRows:
            matrix[row] = [0]*cols
        
        for col in seroCols:
            for i in range(rows):
                matrix[i][col] = 0
        
        return matrix


if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    result = Solution().setZeroes(matrix)
    print(result)