matrix = [[1,1,1],[1,0,1],[1,1,1]]

indexs = [] 
for list in matrix:
    if 0 in list:
        indexs.append([matrix.index(list),list.index(0)])

for i in range(len(matrix)):
    if i in [row[0] for row in indexs]:
        matrix[i] = [0]*len(matrix[i])
        continue
    for j in range(len(matrix[i])):
        if j in [row[j] for row in indexs]:
            for k in range(len(matrix)):
                if len(matrix[i]) > j:
                    matrix[k][j] = [0]*len(matrix)
