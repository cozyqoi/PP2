def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]

print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False
