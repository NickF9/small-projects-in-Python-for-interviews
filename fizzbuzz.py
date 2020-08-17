"""
the code returns a string with numbers (separated by a space) in the range from begin to end, inclusive
At the same time:
    →   If the number is divisible by 3 without remainder, the word Fizz is output instead
    →   If the number is divisible by 5 without remainder, the word Buzz is output instead
    →   If the number is divisible by both 3 and 5, the word FizzBuzz is output instead of the number
    →   In all other cases the number itself is added to the string
"""

def fizzbuzz(begin, end):
    counter = ''
    if begin < end:
        while begin <= end:
            if begin % 3 == 0 and begin % 5 == 0:
                counter = counter + " " + 'FizzBuzz'
            elif begin % 5 == 0:
                counter = counter + " " + 'Buzz'
            elif begin % 3 == 0:
                counter = counter + " " + 'Fizz'
            else:
                counter = counter + ' ' + str(begin)
            begin += 1
        print(counter[1:])
    else:
        print('Incorrect input')


begin = int(input('Input the digit to start the sequence with: '))
end = int(input('Input the digit to end the sequence with: '))
fizzbuzz(begin, end)