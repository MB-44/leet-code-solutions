# def reverse(x):
#     if x < (-2**31) or x > ((2**31)-1):
#         return 0
#     elif str(x)[0]=="-":
#         output = str(x)[1:]
#         output = int(output[::-1].strip("0"))
#         return output-(output*2)
#     else: 
#         output = int((str(x)[::-1]).strip("0"))
#         return output

def reverse(self,x: int):
    def signCheck(num):
        if num>0:
            return 1
        else: 
            return -1
    sign = signCheck(x)
    reverse = str(abs(x))[::-1]
    num = sign * reverse

    if abs(num) > (2 ** 31 -1):
        return 0
    else: 
        return num