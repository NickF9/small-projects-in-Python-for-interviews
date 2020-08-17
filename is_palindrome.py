"""
the code takes a word as input, determines whether it is a palindrome, and returns a Boolean value
"""
def is_palindrome(string):
    x = len(string)
    i = 0
    j = x - 1
    if x == 1:
        print(True)
    elif x == 2:
        if string[i] == string[j]:
            print(True)
        else:
            print(False)
    else:
        while i != j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                break
        print(string[i] == string[j])

string = input('Input the word palindrome to check: ')
is_palindrome(string)