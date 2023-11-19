# Run time - 14ms
# Memory - 13.25MB

def kidsWithCandies(candies,extraCandies):
    result = []
    m = max(candies)
    for kid in candies:
        if kid+extraCandies >= m:
            result.append(True)
        else: 
            result.append(False)
    return result

x = kidsWithCandies([2,3,5,1,3],3)
print(x)