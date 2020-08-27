def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

string = input('Input some palindrome: ')

string = string.lower().replace(' ', '')
symbols = ['/', '|', '\\', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '"', '_', '<', '>', '?', ',', '.', '[', ']', '{', '}', '`', '~', "'"]
for i in range(len(symbols)):
    string = string.replace(symbols[i], '')

if (is_palindrome(string)):
    print('Yes, it\'s a palindrom!')
else:
    print('No, it\'s not a palindrom!')