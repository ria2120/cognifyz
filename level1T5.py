def is_palindrome(s):
    s = s.lower()  
    s = ''.join(filter(str.isalnum, s))  
    return s == s[::-1]

test_strings = [
    "madam",
    "rose",
    "ria",
    "palindrome",
]

for string in test_strings:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')