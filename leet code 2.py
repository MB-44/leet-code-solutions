# Roman to Integer

def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    temp, total = 0, 0
    romanBackList = list(roman)[::-1]
    for c in romanBackList:
        if temp == 0:
            total += dict[c]
        elif temp > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        temp = dict[c]
    return total
print(solution("MCMXCIV"))