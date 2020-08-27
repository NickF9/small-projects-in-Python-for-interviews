def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Input some palindrome: ')

if (is_palindrome(something)):
    print('Yes, it\'s a palindrom!')
else:
    print('No, it\'s not a palindrom!')