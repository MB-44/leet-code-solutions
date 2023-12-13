# not this one
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
        
        rows = []
        cols = []

        for item in indexs:
            rows.append(item[0]), cols.append(item[1])

        uniqueRows = list(set(rows))
        uniqueCols = list(set(cols))

        mightBe01 = []
        for i,j in zip(uniqueRows,uniqueCols):
            if rows.count(i) == 1 and cols.count(j) == 1:
                mightBe01.append([i,j])
        
        count = 0
        for item in mightBe01:
            if mat[item[0]][item[1]] == 1:
                count += 1
        return count


class Solution:
    def numSpecial(self, nums: list[list[int]]) -> int:
        result = 0
        columns = [0] * len(nums[0])

        for i in range(len(nums)):
            ones_in_the_row = 0
            column = 0

            for j in range(len(nums[i])):
                if nums[i][j] == 1:
                    ones_in_the_row += 1

                    if ones_in_the_row == 1:
                        columns[j] = 1 if columns[j] == 0 else 2
                        column = j
                    else:
                        columns[column] = 2
                        columns[j] = 2

        result += sum(column == 1 for column in columns)
        return result        