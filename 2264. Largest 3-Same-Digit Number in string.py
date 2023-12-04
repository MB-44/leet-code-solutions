class Solution:
    def largestGoodInteger(num: str) -> str:
        num1, uniNums = list(num), list(set(num))
        max3nums = []
        output = "-1"

        for n1 in uniNums:
            count = num.count(n1)
            if count >= 3:
                for _ in range(count-2):
                    index = num1.index(n1)
                    subString = num1[index:index+3]

                    if subString == n1*3 and int(n1) > int(output):
                        output = str(n1)
                    num1.pop(index)

        if output == "-1":
            return f""
        return f"{output*3}"

if __name__ == "__main__":
    num = "6777133339"
    x = Solution.largestGoodInteger(num)
    print(x)