"""
the code outputs the only for even numbers of the Fibonacci sequence up to the specified sequence element
"""
def fibo_dev(digit):
    fi0 = 0
    fi1 = 1
    counter = ''
    ques = int(input('Should start calculating the sequence from 0 or 1?' + '\n' + '(Input 0 or 1): '))
    if ques == 0:
        while digit > 0:
            if fi0 % 2 == 0:
                counter += (' ' + str(fi0))
            fi_s = fi0 + fi1
            fi0 = fi1
            fi1 = fi_s
            digit -= 1
        print(counter)
    elif ques == 1:
        while digit > 0:
            fi_s = fi0 + fi1
            fi0 = fi1
            fi1 = fi_s
            if fi0 % 2 == 0:
                counter += (' ' + str(fi0))
            digit -= 1
        print(counter)



digit = int(input('Input the index of the Fibonacci number to which you want to count the sequence (only for even numbers)' + '\n' + '\"index is mean the ordinal number of the Fibonacci number in the Fibonacci sequence\": '))
fibo_dev(digit)