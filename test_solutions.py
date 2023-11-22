# my_string = "123"
# num = 0
# for ch in my_string:
#     if "0" <= ch <= "9":
#         num = num * 10 +(ord(ch) - ord("0"))
# print(type(num))

words = ["one.two.three","four.five","six"]
separator = "."
returnStr = []
for word in words:
    returnStr.extend(word.split("."))
print(returnStr)

