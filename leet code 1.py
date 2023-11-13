l1,l2 = [2,4,3],[9,5,4]
l1.sort(reverse=True),l2.sort(reverse=True)

# strings = [str(integer) for integer in l1]
# aString = "".join(strings)
# anInteger = int(aString)
l1Integer = int("".join([str(integer) for integer in l1]))
l2Integer = int("".join([str(integer) for integer in l2]))

outputList=[]
output = l1Integer+l2Integer;
print(output)
for integer in str(output):
    outputList.insert(0,int(integer))
print(outputList)