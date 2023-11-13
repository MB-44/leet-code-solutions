def isHappy(n:int):
    while n!=1:
        sums = sum([int(digit)**2 for digit in str(n)])
        if sums==4:
            return False
        n=sums
    return True
print(isHappy(4)) 