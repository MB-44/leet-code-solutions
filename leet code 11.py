def plusOne(digits: list[int]) -> list[int]:
    integer=""
    for digit in digits:
        integer += str(digit)
    integer=int(integer)+1
    return [int(digit) for digit in str(integer)]
print(plusOne([1,2,3]))