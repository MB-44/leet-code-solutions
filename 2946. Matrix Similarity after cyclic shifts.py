class Solution:
    def areSimilar(mat,k):
        mat1 = mat
        firstRow = mat[0]
        
        if (len(mat) == 1 and len(mat[0]) == 1) or all(row == firstRow for row in mat) or k==len(firstRow):
            return True
        
        n = len(mat)
        if k > len(firstRow):
            k = k % len(mat[0])

        for i in range(n):
            if len(set(mat[i])) == 1:
                continue

            if (i%2 == 0):
                mat[i] = mat[i][k:] + mat[i][:k]
                continue
            mat[i] = mat[i][-k:] + mat[i][:-k] 
        
        return all(row1 == row2 for row1,row2 in zip(mat1, mat))


if __name__ == "__main__":
    mat = [[2]]
    k = 1
    result = Solution.areSimilar(mat,k)
    print(result)