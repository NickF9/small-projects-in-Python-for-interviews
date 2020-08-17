"""
the code calculates the factorial of the input number
"""

def factorial(digit):
    if digit < 0:
        print('You inputed a negative digit "' + str(digit) + '" , perhaps you meant: ' + str(abs(digit)))
        ques = input('Input yes/no: ')
        if ques == 'yes':
            digit = abs(digit)
            factorial(digit)
        elif ques == 'no':
            print(False)
    else:
        multiply = 1
        digit_new = digit
        while digit_new > 0:
            multiply = multiply * digit_new
            digit_new = digit_new - 1
        print('The factorial of ' + str(digit) + ' is equal to ' + str(multiply))

digit = int(input('Input a digit to calculate the factorial for: '))
factorial(digit)