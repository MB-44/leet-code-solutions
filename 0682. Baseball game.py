class Solution:
    def calPoints(operations: list[str]) -> int:
        points = []
        index = 0
        for op in operations:
            if op.isnumeric():
                points.append(int(op))
            elif op == "C":
                points.pop()
            elif op == "D":
                points.append(points[index-1]*points[index-2])
            elif op == "+":
                points.append(points[index-1]+points[index-2])

        return sum(points)

ops = ["5","2","C","D","+"]
result = Solution.calPoints(ops)
print(result)