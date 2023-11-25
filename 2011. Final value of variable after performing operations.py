class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0
        for i in range(len(operations)):
            if "--" in operations[i]:
                X -= 1
                continue
            X += 1
        return X


if __name__ == "__main__":
    operations = ["--X","X++","X++"]
    result = Solution().finalValueAfterOperations(operations)
    print(result)