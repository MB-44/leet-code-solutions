class Solution(object):
    def checkStraightLine(self,coordinates):
        flag = True
        for i in range(2,len(coordinates)):
            y1, x1 = (coordinates[i-1][1] - coordinates[i-2][1]), (coordinates[i-1][0] - coordinates[i-2][0])
            y2, x2 = (coordinates[i][1] - coordinates[i-1][1]), (coordinates[i][0] - coordinates[i-1][0])
            
            if x1 == 0 or x2 == 0:
                x1,x2 = 1,1
            
            if y1/x1 != y2/x2:
                flag = False

        return flag