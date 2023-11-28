str = "101"
dec,x = 0,0
for i in str[::-1]:
    dec += (2**x)*int(i)
    x += 1
print(dec)