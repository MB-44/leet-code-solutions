class Solution:
    def selfDividingNumbers(left,right):
        output = []
        for i in range(left,right+1):
            if i%10 == 0:
                continue
            if i > 10:
                digits = [int(digit) for digit in str(i)]
                valid = True
                for digit in digits:
                    if i%digit != 0:
                        valid = False
                if valid:
                    output.append(i)
            else: 
                output.append(i)
        return list(set(output))

left = 1
right = 22
result = Solution.selfDividingNumbers(left,right)
print(result)