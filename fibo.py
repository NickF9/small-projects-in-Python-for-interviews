"""
the code outputs the Fibonacci sequence up to the specified sequence element
"""
def fibo(digit):
    fi0 = 0
    fi1 = 1
    counter = ''
    ques = int(input('Should start calculating the sequence from 0 or 1?' + '\n' + '(Input 0 or 1): '))
    if ques == 0:
        while digit > 0:
            counter += (' ' + str(fi0))
            fi_s = fi0 + fi1
            fi0 = fi1
            fi1 = fi_s
            digit -= 1
        print(counter[1:])
    elif ques == 1:
        while digit > 0:
            fi_s = fi0 + fi1
            fi0 = fi1
            fi1 = fi_s
            digit -= 1
            counter += (' ' + str(fi0))
        print(counter[1:])

digit = int(input('Input the index of the Fibonacci number to which you want to count the sequence' + '\n' + '(index is mean the ordinal number of the Fibonacci number in the Fibonacci sequence): '))
fibo(digit)