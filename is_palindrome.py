"""
the code takes a word as input, determines whether it is a palindrome, and returns a Boolean value
"""
def is_palindrome(string):
    x = len(string)
    i = 0
    j = x - 1
    new_i = i
    new_j = j
    if x == 1:
        print(True)
    elif x == 2:
        if string[i] == string[j]:
            print(True)
        else:
            print(False)
    else:
        while new_i != new_j:
            if string[new_i] == string[new_j]:
                new_i += 1
                new_j -= 1
                if i == new_j and j == new_i:
                    break
            else:
                break
        print(string[new_i] == string[new_j])

string = input('Input the word palindrome to check: ')
is_palindrome(string)
