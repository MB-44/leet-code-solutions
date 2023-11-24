class Solution(object):
    def largestValues(self,root):
        def getTreeRows(root):
            if not root:
                return 0
            
            leftSide = getTreeRows(root.left)
            rightSide = getTreeRows(root.right)

            return max(leftSide,rightSide)+1
        output = [root[0]]

        for i in range(2,2**getTreeRows()-1):
            pass # continue in here



if __name__ == "__main__":
    root = [1,3,2,5,3,"x",9]
    result = Solution().largestValues(root)
    print(result)
