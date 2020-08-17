"""
the code converts numbers from binary to decimal
"""

def revers(result):
    x = len(result) - 1
    revers_digits = ''
    while x >= 0:
        revers_digits = revers_digits + str(result)[x]
        x -= 1
    print(revers_digits)

def binary(digit):
    result = ''
    if digit < 0:
        digit *= -1
    elif digit == 0:
        return 0
    else:
        while digit > 0:
            new_result = digit % 2
            result = result + str(new_result)
            digit = digit // 2
        return revers(result)

digit = int(input('Input a number in the decimal system to convert it to binary: '))
binary(digit)